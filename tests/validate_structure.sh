#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

required_files=(
  "README.md"
  "LICENSE"
  "CLAUDE.md"
  "install.sh"
  "install-custom.sh"
  "skill/SKILL.md"
  "skill/market-positioning.md"
  "skill/validation.md"
  "skill/offer-pricing.md"
  "skill/acquisition.md"
  "skill/hackathon-grants.md"
  "skill/proof-assets.md"
  "skill/objection-map.md"
  "skill/win-loss.md"
  "skill/resources.md"
  "agents/founder-strategist.md"
  "agents/gtm-operator.md"
  "agents/grant-submission-coach.md"
  "agents/proof-writer.md"
  "commands/founder-sprint.md"
  "commands/validate-demand.md"
  "commands/grant-submission.md"
  "commands/proof-assets.md"
  "rules/founder-evidence.md"
)

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

for file in "${required_files[@]}"; do
  [[ -f "$ROOT_DIR/$file" ]] || fail "Missing $file"
done

grep -q "^name: solana-founder$" "$ROOT_DIR/skill/SKILL.md" || fail "SKILL.md missing skill name"
grep -q "^description:" "$ROOT_DIR/skill/SKILL.md" || fail "SKILL.md missing description"
grep -q "^user-invocable: true$" "$ROOT_DIR/skill/SKILL.md" || fail "SKILL.md missing user-invocable"

bash -n "$ROOT_DIR/install.sh"
bash -n "$ROOT_DIR/install-custom.sh"
bash -n "$ROOT_DIR/tests/validate_structure.sh"

while IFS= read -r link; do
  target="${link#](}"
  target="${target%)}"
  if [[ "$target" == http* || "$target" == \#* ]]; then
    continue
  fi
  if [[ "$target" == *.md ]]; then
    [[ -f "$ROOT_DIR/skill/$target" ]] || fail "Broken skill link: $target"
  fi
done < <(grep -oE '\]\([^)]+\.md\)' "$ROOT_DIR/skill/SKILL.md" || true)

echo "OK: solana-founder-skill structure is valid"
