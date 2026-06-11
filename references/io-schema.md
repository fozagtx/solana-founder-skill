# Pharos NFT Appraisal IO Schema

## Input

```json
{
  "prompt": "Appraise this Pharos NFT contract: 0x0000000000000000000000000000000000000000",
  "contract_address": "0x0000000000000000000000000000000000000000",
  "network": "pharos",
  "rpc_url": "optional custom Pharos RPC URL",
  "openai_api_key": "optional",
  "timeout_seconds": 20
}
```

Supported networks:

- `pharos`
- `pharos-atlantic`
- `pharos-mainnet`

Default network: live Pharos mainnet RPC.

## Output

```json
{
  "schema_version": "1.0",
  "status": "success",
  "skill": "nft_appraisal_skill",
  "source": "pharos-json-rpc",
  "target": {
    "network": "pharos-mainnet",
    "chain_id": 1672,
    "contract_address": "0x...",
    "rpc_url": "https://rpc.pharos.xyz/",
    "explorer_url": null
  },
  "collection": {
    "address": "0x...",
    "name": "string-or-null",
    "symbol": "string-or-null",
    "token_standard": "ERC721|ERC1155|unknown",
    "total_supply": 10000,
    "contract_uri": "string-or-null",
    "metadata_available": true
  },
  "interfaces": {
    "ERC721": true,
    "ERC721Metadata": true,
    "ERC1155": false,
    "ERC1155MetadataURI": false
  },
  "appraisal": {
    "summary": "Source-grounded, non-financial Pharos contract appraisal.",
    "confidence": "low|medium",
    "risk_flags": [],
    "limitations": [],
    "market_data": {
      "floor_price": null,
      "currency": null,
      "note": "No Pharos marketplace data source is queried by this skill."
    }
  }
}
```

## Error Codes

- `MISSING_CONTRACT_ADDRESS`
- `INVALID_CONTRACT_ADDRESS`
- `UNSUPPORTED_NETWORK`
- `NOT_CONTRACT`
- `RPC_ERROR`
- `UNSAFE_INPUT`
- `UNEXPECTED_ERROR`
