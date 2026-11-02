#!/usr/bin/env bash
set -euo pipefail

REPO="${AOD_REPO:-or-abdillh/AI-Orchestrated-Development-AOD}"
BRANCH="${AOD_BRANCH:-main}"
TARGET_DIR='.'
TARGET_GIVEN=false
ASSUME_YES=false
FORCE_INTERACTIVE=false
COLOR=true
usage() {
    printf 'Usage: bash install.sh [--yes | --interactive] [--no-color] [project-directory]\n'
    printf '  --yes          Instal tanpa prompt (CI / otomatisasi).\n'
    printf '  --interactive  Wajibkan wizard melalui terminal.\n'
    printf '  --no-color     Matikan warna ANSI; NO_COLOR juga didukung.\n'
}
while [ "$#" -gt 0 ]; do
    case "$1" in
        --yes|-y) ASSUME_YES=true ;;
        --interactive) FORCE_INTERACTIVE=true ;;
        --no-color) COLOR=false ;;
        --help|-h) usage; exit 0 ;;
        --) shift; if [ "$#" -ne 1 ] || "$TARGET_GIVEN"; then usage >&2; exit 1; fi
            TARGET_DIR="$1"; TARGET_GIVEN=true; shift; break ;;
        -*) printf 'Opsi tidak dikenal: %s\n' "$1" >&2; usage >&2; exit 1 ;;
        *) if "$TARGET_GIVEN"; then usage >&2; exit 1; fi
            TARGET_DIR="$1"; TARGET_GIVEN=true ;;
    esac
    shift
done
if "$ASSUME_YES" && "$FORCE_INTERACTIVE"; then
    printf 'Pilih salah satu: --yes atau --interactive.\n' >&2; exit 1
fi

C_CYAN='' C_GREEN='' C_RED='' C_RESET=''
if "$COLOR" && [ -t 1 ] && [ -z "${NO_COLOR+x}" ] && [ "${TERM:-dumb}" != dumb ]; then
    C_CYAN=$'\033[36m'; C_GREEN=$'\033[32m'; C_RED=$'\033[31m'; C_RESET=$'\033[0m'
fi
printf '%s' "$C_CYAN"
printf '%s\n' '
    ___    ____  ____
   /   |  / __ \/ __ \
  / /| | / / / / / / /
 / ___ |/ /_/ / /_/ /
/_/  |_|\____/\____/

 AI-Orchestrated Development
'
printf '%s\n' "$C_RESET"
printf 'Installer skill pack AOD\n\n'

INTERACTIVE=false
if ! "$ASSUME_YES"; then
    if { [ -t 1 ] || "$FORCE_INTERACTIVE"; } && { exec 3<>/dev/tty; } 2>/dev/null; then
        INTERACTIVE=true
    elif "$FORCE_INTERACTIVE"; then
        printf 'Terminal interaktif tidak tersedia. Gunakan --yes untuk otomatisasi.\n' >&2; exit 1
    fi
fi
ask() {
    printf '%s' "$1" >&3
    if ! IFS= read -r ANSWER <&3; then
        printf '\nInput terminal terputus; instalasi dibatalkan.\n' >&2; exit 1
    fi
}
step() { printf '\n%s[%s/5] %s%s\n' "$C_CYAN" "$1" "$2" "$C_RESET"; }
trap 'printf "\n%sInstalasi gagal pada baris %s. Periksa pesan error di atas.%s\n" "$C_RED" "$LINENO" "$C_RESET" >&2' ERR
trap 'printf "\nInstalasi dihentikan.\n" >&2; exit 130' INT TERM

step 1 'Memeriksa kebutuhan runtime'
for dependency in python3 mktemp; do
    command -v "$dependency" >/dev/null 2>&1 || { printf 'Missing dependency: %s\n' "$dependency" >&2; exit 1; }
done
python3 -c 'import sys; assert sys.version_info >= (3, 9), "Python 3.9+ required"'
printf '  [OK] Python 3.9+ dan mktemp tersedia.\n'

step 2 'Memilih direktori proyek'
if "$INTERACTIVE" && ! "$TARGET_GIVEN"; then
    ask 'Direktori proyek [.]: '
    TARGET_DIR="${ANSWER:-.}"
fi
TARGET_DIR="$(python3 -c 'from pathlib import Path; import sys; print(Path(sys.argv[1]).expanduser().resolve())' "$TARGET_DIR")"
printf '  Target: %s\n' "$TARGET_DIR"

step 3 'Menyiapkan sumber paket'
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
if [ -f "$SCRIPT_DIR/.agents/aod-package.json" ]; then
    SOURCE_DIR="$SCRIPT_DIR"
    printf '  Sumber lokal: %s\n' "$SOURCE_DIR"
else
    command -v tar >/dev/null 2>&1 || { echo 'Missing dependency: tar' >&2; exit 1; }
    ARCHIVE_URL="https://github.com/${REPO}/archive/refs/heads/${BRANCH}.tar.gz"
    printf '  Mengunduh %s @ %s ...\n' "$REPO" "$BRANCH"
    if command -v curl >/dev/null 2>&1; then
        curl -fL --progress-bar "$ARCHIVE_URL" -o "$TMP_DIR/aod.tar.gz"
    elif command -v wget >/dev/null 2>&1; then
        wget -O "$TMP_DIR/aod.tar.gz" "$ARCHIVE_URL"
    else
        echo 'Remote installation requires curl or wget' >&2; exit 1
    fi
    printf '  Mengekstrak paket ...\n'
    tar -xzf "$TMP_DIR/aod.tar.gz" -C "$TMP_DIR"
    SOURCE_DIR="$(python3 -c 'from pathlib import Path; import sys; print(next(p.parent.parent for p in Path(sys.argv[1]).glob("*/.agents/aod-package.json")))' "$TMP_DIR")"
fi

step 4 'Meninjau dan memasang paket'
printf '  Paket memperbarui skills, rules, registry, helper, dan template terkelola.\n'
printf '  Instruksi agent diperbarui hanya dalam blok AOD.\n'
printf '  Checkpoint, dokumen produk, file custom dan aturan arsitektur proyek dipertahankan.\n'
if "$INTERACTIVE"; then
    while true; do
        printf '\n  1) Pasang / perbarui di %s\n  2) Ubah direktori target\n  3) Lihat isi paket\n  4) Batal\n' "$TARGET_DIR"
        ask 'Pilihan [1-4]: '
        case "$ANSWER" in
            1) break ;;
            2) ask 'Direktori target baru: '
               if [ -n "$ANSWER" ]; then
                   TARGET_DIR="$(python3 -c 'from pathlib import Path; import sys; print(Path(sys.argv[1]).expanduser().resolve())' "$ANSWER")"
               else printf '  Direktori kosong; target tetap.\n'; fi ;;
            3) python3 -c 'import json,sys; from pathlib import Path; r=Path(sys.argv[1]); m=json.loads((r/".agents/aod-package.json").read_text()); print("\n".join("  "+p for p in m["files"])); print("  + blok instruksi AGENTS, GEMINI, Claude, Copilot, Cursor, Windsurf")' "$SOURCE_DIR" ;;
            4) printf 'Instalasi dibatalkan; file proyek belum diubah.\n'; exit 0 ;;
            *) printf '  Pilih 1, 2, 3, atau 4. Jawaban kosong tidak memulai instalasi.\n' ;;
        esac
    done
else
    printf '  Mode non-interaktif; memasang ke target di atas.\n'
fi
python3 "$SOURCE_DIR/.agents/skills/aod-orchestrator/scripts/install_package.py" "$SOURCE_DIR" "$TARGET_DIR"
step 5 'Instalasi selesai'
printf '%s  [OK] Paket AOD siap di %s%s\n' "$C_GREEN" "$TARGET_DIR" "$C_RESET"
printf '  Buka proyek di coding agent, lalu panggil "Mulai AOD".\n'
printf '  Untuk sesi berikutnya: "Lanjut AOD" atau "Status AOD".\n'
