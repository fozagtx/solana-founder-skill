"""Pharos NFT appraisal skill using Pharos JSON-RPC."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from typing import Any, Dict, Mapping, Optional, Tuple
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


SKILL_NAME = "nft_appraisal_skill"
ADDRESS_RE = re.compile(r"0x[a-fA-F0-9]{40}")
UNSAFE_KEYS = {"headers", "cookies", "proxy", "proxies", "private_key", "seed_phrase", "shell", "command", "file_path"}

PHAROS_NETWORKS = {
    "pharos": {
        "network": "pharos-mainnet",
        "rpc_url": "https://rpc.pharos.xyz/",
        "chain_id": 1672,
        "explorer_url": None,
    },
    "pharos-atlantic": {
        "network": "pharos-atlantic",
        "rpc_url": "https://atlantic.dplabs-internal.com",
        "chain_id": 688689,
        "explorer_url": "https://atlantic.pharosscan.xyz",
    },
    "pharos-mainnet": {
        "network": "pharos-mainnet",
        "rpc_url": "https://rpc.pharos.xyz/",
        "chain_id": 1672,
        "explorer_url": None,
    },
}

NETWORK_ALIASES = {
    "pharos": "pharos-mainnet",
    "atlantic": "pharos-atlantic",
    "pharos atlantic": "pharos-atlantic",
    "pharos-atlantic": "pharos-atlantic",
    "mainnet": "pharos-mainnet",
    "pharos mainnet": "pharos-mainnet",
    "pharos-mainnet": "pharos-mainnet",
}

SELECTORS = {
    "name": "0x06fdde03",
    "symbol": "0x95d89b41",
    "total_supply": "0x18160ddd",
    "contract_uri": "0xe8a3d485",
    "supports_interface": "0x01ffc9a7",
}
INTERFACES = {
    "ERC721": "0x80ac58cd",
    "ERC721Metadata": "0x5b5e139f",
    "ERC1155": "0xd9b67a26",
    "ERC1155MetadataURI": "0x0e89341c",
}


class SkillError(Exception):
    """Stable skill error."""

    def __init__(self, code: str, message: str, status: str = "error", retryable: bool = False) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.status = status
        self.retryable = retryable


def run(*args: Any, **kwargs: Any) -> Dict[str, Any]:
    """Run Pharos NFT contract appraisal."""

    generated_at = _now_iso()
    try:
        metadata = _coerce_metadata(args, kwargs)
        _reject_unsafe(metadata)
        target, extraction = _extract_target(metadata)
        network = _network_config(target["network"], metadata)
        timeout = _clamp_int(metadata.get("timeout_seconds", 20), 5, 60)

        chain_id = _rpc(network["rpc_url"], "eth_chainId", [], timeout)
        code = _rpc(network["rpc_url"], "eth_getCode", [target["contract_address"], "latest"], timeout)
        if not code or code == "0x":
            raise SkillError("NOT_CONTRACT", "No contract bytecode found at this address on Pharos.")

        interfaces = _detect_interfaces(network["rpc_url"], target["contract_address"], timeout)
        collection = _read_collection(network["rpc_url"], target["contract_address"], interfaces, timeout)
        appraisal = _appraise(collection, interfaces, network, target["contract_address"])

        return {
            "schema_version": "1.0",
            "status": "success",
            "skill": SKILL_NAME,
            "source": "pharos-json-rpc",
            "request_id": metadata.get("request_id"),
            "generated_at": generated_at,
            "extraction": extraction,
            "target": {
                "network": network["network"],
                "chain_id": _hex_to_int(chain_id),
                "contract_address": target["contract_address"],
                "rpc_url": _redact_url(network["rpc_url"]),
                "explorer_url": network.get("explorer_url"),
            },
            "collection": collection,
            "interfaces": interfaces,
            "appraisal": appraisal,
            "citations": [
                {
                    "provider": "Pharos JSON-RPC",
                    "methods": ["eth_chainId", "eth_getCode", "eth_call"],
                    "network": network["network"],
                    "contract_address": target["contract_address"],
                }
            ],
            "errors": [],
        }
    except SkillError as exc:
        return _error(exc.code, exc.message, exc.status, exc.retryable, generated_at)
    except Exception as exc:  # pragma: no cover
        return _error("UNEXPECTED_ERROR", str(exc), "error", False, generated_at)


def _coerce_metadata(args: Tuple[Any, ...], kwargs: Mapping[str, Any]) -> Dict[str, Any]:
    metadata: Dict[str, Any] = {}
    if args:
        if len(args) == 1 and isinstance(args[0], Mapping):
            metadata.update(dict(args[0]))
        elif len(args) == 1 and isinstance(args[0], str):
            metadata["prompt"] = args[0]
        else:
            raise SkillError("INVALID_METADATA", "run accepts a metadata dict or prompt string.")
    nested = kwargs.get("metadata")
    if isinstance(nested, Mapping):
        metadata.update(dict(nested))
    for key, value in kwargs.items():
        if key != "metadata":
            metadata[key] = value
    return metadata


def _reject_unsafe(metadata: Mapping[str, Any]) -> None:
    found = sorted(key for key in metadata if key in UNSAFE_KEYS)
    if found:
        raise SkillError("UNSAFE_INPUT", f"Unsupported metadata keys: {', '.join(found)}")


def _extract_target(metadata: Mapping[str, Any]) -> Tuple[Dict[str, str], Dict[str, Any]]:
    direct_address = str(metadata.get("contract_address") or "").strip()
    direct_network = str(metadata.get("network") or metadata.get("chain") or "pharos").strip()
    if direct_address:
        return {
            "contract_address": _validate_address(direct_address),
            "network": _normalize_network(direct_network),
        }, {"method": "metadata", "warnings": []}

    prompt = str(metadata.get("prompt") or metadata.get("user_prompt") or "").strip()
    if not prompt:
        raise SkillError("MISSING_CONTRACT_ADDRESS", "Provide a prompt or contract_address.")

    openai_key = _api_key(metadata, "openai", "OPENAI_API_KEY")
    if openai_key:
        extracted = _extract_with_openai(prompt, openai_key)
        if extracted:
            try:
                return {
                    "contract_address": _validate_address(str(extracted.get("contract_address") or "")),
                "network": _normalize_network(str(extracted.get("network") or direct_network)),
                }, {"method": "openai", "warnings": []}
            except SkillError:
                pass

    address_match = ADDRESS_RE.search(prompt)
    if not address_match:
        raise SkillError("MISSING_CONTRACT_ADDRESS", "Could not find an NFT contract address in the prompt.")
    return {
        "contract_address": _validate_address(address_match.group(0)),
        "network": _detect_network(prompt) or "pharos-mainnet",
    }, {"method": "regex", "warnings": ["Used regex fallback. Defaulted to Pharos mainnet when no Pharos network was named."]}


def _extract_with_openai(prompt: str, api_key: str) -> Optional[Dict[str, str]]:
    payload = {
        "model": os.getenv("OPENAI_EXTRACT_MODEL", "gpt-4o-mini"),
        "response_format": {"type": "json_object"},
        "messages": [
            {
                "role": "system",
                "content": (
                    "Extract JSON only: {\"contract_address\": string|null, "
                    "\"network\": \"pharos-mainnet\"|\"pharos-atlantic\"|null}. "
                    "This skill supports Pharos networks only."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0,
    }
    request = Request(
        "https://api.openai.com/v1/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}", "User-Agent": f"{SKILL_NAME}/0.1.0"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=20) as response:
            body = json.loads(response.read().decode("utf-8"))
        return json.loads(body["choices"][0]["message"]["content"])
    except Exception:
        return None


def _validate_address(address: str) -> str:
    if not ADDRESS_RE.fullmatch(address or ""):
        raise SkillError("INVALID_CONTRACT_ADDRESS", "Contract address must be 0x followed by 40 hex characters.")
    return address


def _normalize_network(network: str) -> str:
    raw = " ".join(str(network or "").lower().replace("_", " ").split())
    if raw in NETWORK_ALIASES:
        return NETWORK_ALIASES[raw]
    if not raw:
        return "pharos-mainnet"
    raise SkillError("UNSUPPORTED_NETWORK", "This skill supports Pharos networks only.")


def _detect_network(prompt: str) -> Optional[str]:
    lowered = prompt.lower()
    if re.search(r"\batlantic\b", lowered):
        return "pharos-atlantic"
    if re.search(r"\bmainnet\b", lowered):
        return "pharos-mainnet"
    if re.search(r"\bpharos\b", lowered):
        return "pharos-mainnet"
    named_network = re.search(r"\bon\s+([a-z][a-z0-9-]*)\b", lowered)
    if named_network:
        raise SkillError("UNSUPPORTED_NETWORK", "This skill supports Pharos networks only.")
    return None


def _network_config(network_name: str, metadata: Mapping[str, Any]) -> Dict[str, Any]:
    config = dict(PHAROS_NETWORKS[network_name])
    rpc_url = str(metadata.get("rpc_url") or os.getenv("PHAROS_RPC_URL") or "").strip()
    if rpc_url:
        config["rpc_url"] = rpc_url
        config["network"] = network_name
    return config


def _detect_interfaces(rpc_url: str, contract_address: str, timeout: int) -> Dict[str, bool]:
    return {
        name: _supports_interface(rpc_url, contract_address, interface_id, timeout)
        for name, interface_id in INTERFACES.items()
    }


def _supports_interface(rpc_url: str, contract_address: str, interface_id: str, timeout: int) -> bool:
    data = SELECTORS["supports_interface"] + interface_id[2:] + ("0" * 56)
    try:
        result = _eth_call(rpc_url, contract_address, data, timeout)
        return bool(int(result, 16))
    except Exception:
        return False


def _read_collection(rpc_url: str, contract_address: str, interfaces: Mapping[str, bool], timeout: int) -> Dict[str, Any]:
    name = _safe_string_call(rpc_url, contract_address, SELECTORS["name"], timeout)
    symbol = _safe_string_call(rpc_url, contract_address, SELECTORS["symbol"], timeout)
    total_supply = _safe_uint_call(rpc_url, contract_address, SELECTORS["total_supply"], timeout)
    contract_uri = _safe_string_call(rpc_url, contract_address, SELECTORS["contract_uri"], timeout)
    token_standard = _token_standard(interfaces)
    return {
        "address": contract_address,
        "name": name,
        "symbol": symbol,
        "token_standard": token_standard,
        "total_supply": total_supply,
        "contract_uri": contract_uri,
        "metadata_available": any(value is not None for value in (name, symbol, total_supply, contract_uri)),
    }


def _token_standard(interfaces: Mapping[str, bool]) -> str:
    if interfaces.get("ERC721"):
        return "ERC721"
    if interfaces.get("ERC1155"):
        return "ERC1155"
    return "unknown"


def _safe_string_call(rpc_url: str, contract_address: str, selector: str, timeout: int) -> Optional[str]:
    try:
        return _decode_string(_eth_call(rpc_url, contract_address, selector, timeout))
    except Exception:
        return None


def _safe_uint_call(rpc_url: str, contract_address: str, selector: str, timeout: int) -> Optional[int]:
    try:
        value = _eth_call(rpc_url, contract_address, selector, timeout)
        return int(value, 16) if value and value != "0x" else None
    except Exception:
        return None


def _eth_call(rpc_url: str, contract_address: str, data: str, timeout: int) -> str:
    return _rpc(rpc_url, "eth_call", [{"to": contract_address, "data": data}, "latest"], timeout)


def _rpc(rpc_url: str, method: str, params: list[Any], timeout: int) -> Any:
    payload = {"jsonrpc": "2.0", "id": 1, "method": method, "params": params}
    request = Request(
        rpc_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": f"{SKILL_NAME}/0.1.0"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            body = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise SkillError("RPC_ERROR", f"Pharos RPC HTTP {exc.code}.", retryable=500 <= exc.code < 600) from exc
    except URLError as exc:
        raise SkillError("RPC_ERROR", f"Pharos RPC request failed: {exc.reason}", retryable=True) from exc
    except json.JSONDecodeError as exc:
        raise SkillError("RPC_ERROR", "Pharos RPC returned invalid JSON.", retryable=True) from exc

    if "error" in body:
        message = body["error"].get("message", "Pharos RPC error") if isinstance(body["error"], Mapping) else str(body["error"])
        raise SkillError("RPC_ERROR", message, retryable=False)
    return body.get("result")


def _decode_string(value: str) -> Optional[str]:
    if not value or value == "0x":
        return None
    raw = value[2:]
    try:
        if len(raw) >= 128:
            length = int(raw[64:128], 16)
            data = raw[128 : 128 + length * 2]
            return bytes.fromhex(data).decode("utf-8", errors="replace").strip("\x00") or None
        decoded = bytes.fromhex(raw).decode("utf-8", errors="replace").strip("\x00")
        return decoded or None
    except Exception:
        return None


def _appraise(collection: Mapping[str, Any], interfaces: Mapping[str, bool], network: Mapping[str, Any], contract_address: str) -> Dict[str, Any]:
    risk_flags = []
    limitations = [
        "This is not financial advice.",
        "This appraisal uses Pharos RPC contract reads only.",
        "No marketplace floor price, sales volume, holder distribution, rarity, or liquidity data is inferred.",
    ]
    if collection.get("token_standard") == "unknown":
        risk_flags.append("unknown_nft_standard")
    if not collection.get("metadata_available"):
        risk_flags.append("metadata_unavailable")
    if collection.get("total_supply") is None:
        risk_flags.append("unknown_total_supply")

    name = collection.get("name") or "this Pharos NFT contract"
    standard = collection.get("token_standard") or "unknown"
    confidence = "medium" if standard != "unknown" and collection.get("metadata_available") else "low"
    return {
        "summary": (
            f"{name} was inspected on {network['network']} at {contract_address}. "
            f"The contract appears to use {standard}. This is a Pharos on-chain metadata appraisal, "
            "not a market-price appraisal."
        ),
        "confidence": confidence,
        "risk_flags": risk_flags,
        "limitations": limitations,
        "interface_checks": dict(interfaces),
        "market_data": {
            "floor_price": None,
            "currency": None,
            "note": "No Pharos marketplace data source is queried by this skill.",
        },
    }


def _api_key(metadata: Mapping[str, Any], name: str, env_name: str) -> str:
    api_keys = metadata.get("api_keys")
    nested = ""
    if isinstance(api_keys, Mapping):
        nested = str(api_keys.get(name) or api_keys.get(f"{name}_api_key") or "").strip()
    return str(metadata.get(f"{name}_api_key") or nested or os.getenv(env_name) or "").strip()


def _hex_to_int(value: Any) -> Optional[int]:
    if isinstance(value, str) and value.startswith("0x"):
        return int(value, 16)
    return None


def _redact_url(url: str) -> str:
    return url.split("?")[0]


def _clamp_int(value: Any, low: int, high: int) -> int:
    try:
        number = int(value)
    except (TypeError, ValueError):
        number = low
    return max(low, min(number, high))


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _error(code: str, message: str, status: str, retryable: bool, generated_at: str) -> Dict[str, Any]:
    return {
        "schema_version": "1.0",
        "status": status,
        "skill": SKILL_NAME,
        "generated_at": generated_at,
        "error": {"code": code, "message": message, "retryable": retryable},
        "errors": [{"code": code, "message": message}],
    }
