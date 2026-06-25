#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/skill"
SKILL_NAME="solana-founder"

print_help() {
  echo "Solana Founder Skill custom installer"
  echo ""
  echo "Usage: ./install-custom.sh"
  echo ""
  echo "Choose a personal, project, or custom skills directory."
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  print_help
  exit 0
fi

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Missing source directory: $SOURCE_DIR" >&2
  exit 1
fi

echo "Solana Founder Skill custom install"
echo ""
echo "Select installation location:"
echo "  1) Personal skills: ~/.claude/skills"
echo "  2) Personal skills: ~/.agents/skills"
echo "  3) Current project: ./.claude/skills"
echo "  4) Current project: ./.agents/skills"
echo "  5) Custom path"
echo "  6) Cancel"
echo ""

read -r -p "Choice [1-6]: " choice

case "$choice" in
  1)
    INSTALL_BASE="$HOME/.claude/skills"
    ;;
  2)
    INSTALL_BASE="$HOME/.agents/skills"
    ;;
  3)
    INSTALL_BASE="./.claude/skills"
    ;;
  4)
    INSTALL_BASE="./.agents/skills"
    ;;
  5)
    read -r -p "Enter skills directory path: " INSTALL_BASE
    if [[ -z "$INSTALL_BASE" ]]; then
      echo "Custom path cannot be empty." >&2
      exit 1
    fi
    ;;
  6)
    echo "Installation cancelled."
    exit 0
    ;;
  *)
    echo "Invalid choice." >&2
    exit 1
    ;;
esac

INSTALL_PATH="$INSTALL_BASE/$SKILL_NAME"

echo ""
echo "Install skill to:"
echo "  $INSTALL_PATH"
echo ""
read -r -p "Proceed? [y/N] " reply
if [[ ! "$reply" =~ ^[Yy]$ ]]; then
  echo "Installation cancelled."
  exit 0
fi

mkdir -p "$INSTALL_BASE"

if [[ -d "$INSTALL_PATH" ]]; then
  read -r -p "Existing skill found. Overwrite? [y/N] " overwrite
  if [[ ! "$overwrite" =~ ^[Yy]$ ]]; then
    echo "Installation cancelled."
    exit 0
  fi
  backup_path="$INSTALL_PATH.backup.$(date +%Y%m%d%H%M%S)"
  cp -R "$INSTALL_PATH" "$backup_path"
  echo "Backed up existing skill to $backup_path"
  rm -rf "$INSTALL_PATH"
fi

mkdir -p "$INSTALL_PATH"
cp -R "$SOURCE_DIR"/. "$INSTALL_PATH"/

echo ""
echo "Install optional config file?"
echo "  1) Copy to ./CLAUDE.md"
echo "  2) Copy to ~/.claude/CLAUDE.md"
echo "  3) Skip"
echo ""
read -r -p "Choice [1-3]: " config_choice

case "$config_choice" in
  1)
    if [[ -f "./CLAUDE.md" ]]; then
      cp "./CLAUDE.md" "./CLAUDE.md.backup.$(date +%Y%m%d%H%M%S)"
    fi
    cp "$SCRIPT_DIR/CLAUDE.md" "./CLAUDE.md"
    ;;
  2)
    mkdir -p "$HOME/.claude"
    if [[ -f "$HOME/.claude/CLAUDE.md" ]]; then
      cp "$HOME/.claude/CLAUDE.md" "$HOME/.claude/CLAUDE.md.backup.$(date +%Y%m%d%H%M%S)"
    fi
    cp "$SCRIPT_DIR/CLAUDE.md" "$HOME/.claude/CLAUDE.md"
    ;;
  3)
    ;;
  *)
    echo "Skipping config install."
    ;;
esac

echo ""
echo "Installed solana-founder skill to:"
echo "  $INSTALL_PATH"
