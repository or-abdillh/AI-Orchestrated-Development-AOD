#!/usr/bin/env bash
# ==============================================================================
# AI-Orchestrated Development (AOD) Framework — Universal Installer
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/or-abdillh/AI-Orchestrated-Development-AOD/main/install.sh | bash
#   curl -fsSL https://raw.githubusercontent.com/or-abdillh/AI-Orchestrated-Development-AOD/main/install.sh | bash -s -- /path/to/project
# ==============================================================================

set -eo pipefail

REPO="${AOD_REPO:-or-abdillh/AI-Orchestrated-Development-AOD}"
BRANCH="${AOD_BRANCH:-main}"
TARGET_DIR="${1:-.}"

# Terminal Colors
C_RESET='\033[0m'
C_BOLD='\033[1m'
C_GREEN='\033[32m'
C_BLUE='\033[34m'
C_CYAN='\033[36m'
C_YELLOW='\033[33m'
C_RED='\033[31m'

print_banner() {
    cat << "EOF"
    ___    ____  ____     ______                                           __  
   /   |  / __ \/ __ \   / ____/________ _____ ___  ___ _      ______  _____/ /__
  / /| | / / / / / / /  / /_  / ___/ __ `/ __ `__ \/ _ \ | /| / / __ \/ ___/ //_/
 / ___ |/ /_/ / /_/ /  / __/ / /  / /_/ / / / / / /  __/ |/ |/ / /_/ / /  / ,<   
/_/  |_|\____/_____/  /_/   /_/   \__,_/_/ /_/ /_/\___/|__/|__/\____/_/  /_/|_|  
EOF
    echo -e "${C_CYAN}    AI-Orchestrated Development (AOD) — Framework Installer${C_RESET}\n"
}

log_info()  { echo -e " ${C_BLUE}ℹ${C_RESET}  $1"; }
log_step()  { echo -e " ${C_CYAN}➜${C_RESET}  $1"; }
log_ok()    { echo -e " ${C_GREEN}✔${C_RESET}  $1"; }
log_warn()  { echo -e " ${C_YELLOW}⚠${C_RESET}  $1"; }
log_error() { echo -e " ${C_RED}✖${C_RESET}  $1"; }

print_banner

# Resolve absolute path for target
mkdir -p "$TARGET_DIR"
TARGET_DIR="$(cd "$TARGET_DIR" && pwd)"
log_info "Target Directory: ${C_BOLD}${TARGET_DIR}${C_RESET}"

TMP_DIR="$(mktemp -d -t aod-install-XXXXXX)"
cleanup() {
    rm -rf "$TMP_DIR"
}
trap cleanup EXIT

# 1. Obtain AOD Source Files
log_step "Mengunduh file arsitektur AOD Framework dari GitHub (${C_BOLD}${REPO}@${BRANCH}${C_RESET})..."

ARCHIVE_URL="https://github.com/${REPO}/archive/refs/heads/${BRANCH}.tar.gz"

if command -v curl >/dev/null 2>&1; then
    curl -fsSL "$ARCHIVE_URL" -o "${TMP_DIR}/aod.tar.gz"
elif command -v wget >/dev/null 2>&1; then
    wget -qO "${TMP_DIR}/aod.tar.gz" "$ARCHIVE_URL"
else
    log_error "Dibutuhkan 'curl' atau 'wget' untuk mengunduh package AOD."
    exit 1
fi

tar -xzf "${TMP_DIR}/aod.tar.gz" -C "$TMP_DIR"
SOURCE_DIR="$(find "$TMP_DIR" -mindepth 1 -maxdepth 1 -type d | head -n 1)"

if [ ! -d "${SOURCE_DIR}/.agents" ]; then
    log_error "Gagal menemukan direktori .agents di repository sumber."
    exit 1
fi
log_ok "Sumber AOD Framework berhasil diunduh."

# 2. Inject .agents (Rules & Skills)
log_step "Menginjeksi aturan (.agents/rules/) dan skill (.agents/skills/)..."
mkdir -p "${TARGET_DIR}/.agents/rules"
mkdir -p "${TARGET_DIR}/.agents/skills"

# Copy rules
cp -R "${SOURCE_DIR}/.agents/rules/"* "${TARGET_DIR}/.agents/rules/"

# Copy skills
cp -R "${SOURCE_DIR}/.agents/skills/"* "${TARGET_DIR}/.agents/skills/"

if [ -f "${SOURCE_DIR}/skills-lock.json" ]; then
    cp "${SOURCE_DIR}/skills-lock.json" "${TARGET_DIR}/skills-lock.json"
fi
log_ok "Seluruh aturan (rules) dan 24+ native skills berhasil dipasang."

# 3. Scaffold docs directory structure
log_step "Membuat scaffold struktur direktori docs/..."
DOCS_SUBDIRS=(
    "business"
    "system-design"
    "ui-architecture"
    "development"
    "testing"
    "proposal"
    "samples"
)

for sub in "${DOCS_SUBDIRS[@]}"; do
    mkdir -p "${TARGET_DIR}/docs/${sub}"
done

# Copy sample study case if available and not existing
if [ -f "${SOURCE_DIR}/docs/samples/STUDY_CASE_DOCUMENT.md" ] && [ ! -f "${TARGET_DIR}/docs/samples/STUDY_CASE_DOCUMENT.md" ]; then
    cp "${SOURCE_DIR}/docs/samples/STUDY_CASE_DOCUMENT.md" "${TARGET_DIR}/docs/samples/STUDY_CASE_DOCUMENT.md"
fi
log_ok "Struktur direktori docs/ berhasil disiapkan."

# 4. Inject AGENTS.md and GEMINI.md declarations
log_step "Mengonfigurasi file instruksi agen (AGENTS.md & GEMINI.md)..."

AOD_CONFIG_BLOCK='<!-- aod:start -->
## AI-Orchestrated Development (AOD)

Untuk memulai atau melanjutkan project dengan metodologi AOD, aktifkan skill yang sesuai:

**Entry Point (Mulai di sini):**
- `aod-orchestrator` — panduan interaktif lengkap fase demi fase, dari discovery hingga UAT.

**Pre-Project:**
- `aod-proposal` — konversi PRD + Tech Spec menjadi Commercial Proposal & Quotation untuk klien.

**Phase 1 – Business Layer:**
- `aod-brd` — Business Requirement Document
- `aod-business-flow` — Business Flow (AS-IS & TO-BE)
- `aod-prd` — Product Requirement Document
- `aod-flowchart` — Mermaid Flowchart Diagram
- `aod-rbac` — Role & Permission Matrix
- `aod-data-dictionary` — Data Dictionary
- `aod-dbml` — DBML Schema Generator

**Phase 2 – System Design:**
- `aod-state-machine` — State Machine Definition
- `aod-api-contract` — API Contract
- `aod-ui-flow` — UI Flow / Screen Map
- `aod-website-concept` — Website Concept Document
- `aod-design-system` — Design System Document
- `aod-ui-style` — UI Style Document

**Phase 3 – UI Architecture:**
- `aod-ui-component-map` — UI Component Map
- `aod-ui-slicing` — Full UI Slicing Document
- `aod-tailwind-config` — CSS Framework / Design Token Config
- `aod-page-slicer` — Per-Page Component Slicer (dijalankan berulang per halaman)

**Phase 4 – Development:**
- `aod-tech-spec` — Technical Specification
- `aod-phase-plan` — Development Phase Plan
- `aod-feature-prompts` — Feature Prompt Library
- `aod-dod` — Definition of Done Checklist

**Phase 5 – Testing:**
- `aod-uat` — UAT Sheet Generator

**AOD Core Rules (Always Active):**
- Disiplin fase ketat: ikuti urutan Business Layer → System Design → UI Architecture → Development → Testing.
- Dependency chain mutlak: jangan membuat dokumen turunan tanpa dokumen prasyarat.
- AI berperan sebagai executor terkendali, bukan arsitek independen.
- Document versioning mutlak: seluruh dokumen di `docs/` wajib memiliki header semantic versioning (`vMAJOR.MINOR.PATCH`), tanggal `Last Updated`, dan tabel `Revision History`. AI wajib menaikkan versi (Major/Minor/Patch) setiap kali melakukan perubahan dokumen.
- Git feature-branching mutlak: seluruh implementasi pada Phase 4 wajib berada di branch terpisah (`phase/<num>-<slug>` atau `feat/<module>-<slug>`). Dilarang commit langsung ke `main`/`master`. Gunakan `smart-git-commit` untuk commit atomik.
<!-- aod:end -->'

inject_file() {
    local target_file="$1"
    if [ ! -f "$target_file" ]; then
        echo -e "$AOD_CONFIG_BLOCK\n" > "$target_file"
        log_ok "Membuat file baru: ${target_file}"
    elif grep -q "<!-- aod:start -->" "$target_file"; then
        # Replace existing block
        node -e '
            const fs = require("fs");
            const file = process.argv[1];
            const replacement = process.argv[2];
            let content = fs.readFileSync(file, "utf8");
            content = content.replace(/<!-- aod:start -->[\s\S]*?<!-- aod:end -->/m, replacement);
            fs.writeFileSync(file, content, "utf8");
        ' "$target_file" "$AOD_CONFIG_BLOCK" 2>/dev/null || true
        log_ok "Memperbarui konfigurasi AOD di: ${target_file}"
    else
        echo -e "\n\n$AOD_CONFIG_BLOCK\n" >> "$target_file"
        log_ok "Menambahkan blok AOD ke: ${target_file}"
    fi
}

inject_file "${TARGET_DIR}/AGENTS.md"
inject_file "${TARGET_DIR}/GEMINI.md"

echo ""
echo -e "${C_GREEN}${C_BOLD}🎉 Instalasi AOD Framework Berhasil!${C_RESET}\n"
echo -e "Untuk mulai menjalankan AOD pada AI coding agent Anda:"
echo -e " 1. Buka AI Assistant / Antigravity di proyek ini."
echo -e " 2. Ketik prompt: ${C_BOLD}\"Mulai AOD\"${C_RESET} atau ${C_BOLD}\"Jalankan aod-orchestrator\"${C_RESET}."
echo -e " 3. AI akan otomatis membaca panduan fase dan memandu pengerjaan secara terstruktur."
echo ""
