#!/usr/bin/env bash
set -euo pipefail

REPO="${AOD_REPO:-or-abdillh/AI-Orchestrated-Development-AOD}"
BRANCH="${AOD_BRANCH:-main}"
TARGET_DIR="${1:-.}"
for dependency in python3 mktemp; do
    command -v "$dependency" >/dev/null 2>&1 || { printf 'Missing dependency: %s\n' "$dependency" >&2; exit 1; }
done
python3 -c 'import sys; assert sys.version_info >= (3, 9), "Python 3.9+ required"'
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
if [ -f "$SCRIPT_DIR/.agents/aod-package.json" ]; then
    SOURCE_DIR="$SCRIPT_DIR"
else
    command -v tar >/dev/null 2>&1 || { echo 'Missing dependency: tar' >&2; exit 1; }
    ARCHIVE_URL="https://github.com/${REPO}/archive/refs/heads/${BRANCH}.tar.gz"
    if command -v curl >/dev/null 2>&1; then
        curl -fsSL "$ARCHIVE_URL" -o "$TMP_DIR/aod.tar.gz"
    elif command -v wget >/dev/null 2>&1; then
        wget -qO "$TMP_DIR/aod.tar.gz" "$ARCHIVE_URL"
    else
        echo 'Remote installation requires curl or wget' >&2; exit 1
    fi
    tar -xzf "$TMP_DIR/aod.tar.gz" -C "$TMP_DIR"
    SOURCE_DIR="$(python3 -c 'from pathlib import Path; import sys; print(next(p.parent.parent for p in Path(sys.argv[1]).glob("*/.agents/aod-package.json")))' "$TMP_DIR")"
fi
python3 "$SOURCE_DIR/.agents/skills/aod-orchestrator/scripts/install_package.py" "$SOURCE_DIR" "$TARGET_DIR"
printf 'Ready: panggil "Mulai AOD"; resume dengan "Lanjut AOD".\n'
