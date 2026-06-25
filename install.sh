#!/usr/bin/env bash

set -euo pipefail

SKIP_CONFIRM=false
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/skill"
SKILL_NAME="solana-founder"
DEFAULT_SKILLS_DIR="$HOME/.claude/skills"
DEFAULT_INSTALL_PATH="$DEFAULT_SKILLS_DIR/$SKILL_NAME"
DEFAULT_CONFIG_DIR="$HOME/.claude"
DEFAULT_CONFIG_PATH="$DEFAULT_CONFIG_DIR/CLAUDE.md"

print_help() {
  echo "Solana Founder Skill installer"
  echo ""
  echo "Usage: ./install.sh [OPTIONS]"
  echo ""
  echo "Options:"
  echo "  -y, --yes      Install with defaults without prompting"
  echo "  -h, --help     Show this help"
  echo ""
  echo "Defaults:"
  echo "  Skill:  $DEFAULT_INSTALL_PATH"
  echo "  Config: $DEFAULT_CONFIG_PATH"
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    -y|--yes)
      SKIP_CONFIRM=true
      shift
      ;;
    -h|--help)
      print_help
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      print_help
      exit 1
      ;;
  esac
done

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Missing source directory: $SOURCE_DIR" >&2
  exit 1
fi

echo "Solana Founder Skill"
echo ""
echo "This will install:"
echo "  Skill files -> $DEFAULT_INSTALL_PATH"
echo "  Config      -> $DEFAULT_CONFIG_PATH"
echo ""

if [[ "$SKIP_CONFIRM" != "true" ]]; then
  read -r -p "Proceed? [Y/n] " reply
  if [[ "$reply" =~ ^[Nn]$ ]]; then
    echo "Installation cancelled."
    exit 0
  fi
fi

mkdir -p "$DEFAULT_INSTALL_PATH"
mkdir -p "$DEFAULT_CONFIG_DIR"

if [[ -f "$DEFAULT_INSTALL_PATH/SKILL.md" ]]; then
  backup_path="$DEFAULT_INSTALL_PATH.backup.$(date +%Y%m%d%H%M%S)"
  cp -R "$DEFAULT_INSTALL_PATH" "$backup_path"
  echo "Backed up existing skill to $backup_path"
fi

rm -rf "$DEFAULT_INSTALL_PATH"
mkdir -p "$DEFAULT_INSTALL_PATH"
cp -R "$SOURCE_DIR"/. "$DEFAULT_INSTALL_PATH"/

if [[ -f "$SCRIPT_DIR/CLAUDE.md" ]]; then
  if [[ -f "$DEFAULT_CONFIG_PATH" ]]; then
    cp "$DEFAULT_CONFIG_PATH" "$DEFAULT_CONFIG_PATH.backup.$(date +%Y%m%d%H%M%S)"
  fi
  cp "$SCRIPT_DIR/CLAUDE.md" "$DEFAULT_CONFIG_PATH"
fi

echo ""
echo "Installed solana-founder skill to:"
echo "  $DEFAULT_INSTALL_PATH"
echo ""
echo "Try:"
echo "  Help me validate this Solana devtool before I build more."
