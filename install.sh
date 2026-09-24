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
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd || true)"

if [ -n "$SCRIPT_DIR" ] && [ -d "${SCRIPT_DIR}/.agents" ] && [ "$SCRIPT_DIR" != "$TARGET_DIR" ]; then
    log_step "Menggunakan file AOD Framework dari sumber lokal (${C_BOLD}${SCRIPT_DIR}${C_RESET})..."
    SOURCE_DIR="$SCRIPT_DIR"
    log_ok "Sumber lokal AOD Framework terdeteksi."
else
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
fi


# 2. Inject .agents (Rules & Skills)
log_step "Menginjeksi aturan (.agents/rules/) dan skill (.agents/skills/)..."
mkdir -p "${TARGET_DIR}/.agents/rules"
mkdir -p "${TARGET_DIR}/.agents/skills"

# Copy rules (preserve custom aod-architecture-engineering.md if it already exists)
for rule_file in "${SOURCE_DIR}/.agents/rules/"*; do
    if [ -f "$rule_file" ]; then
        rule_name="$(basename "$rule_file")"
        if [ "$rule_name" = "aod-architecture-engineering.md" ] && [ -f "${TARGET_DIR}/.agents/rules/${rule_name}" ]; then
            log_info "Mempertahankan aturan arsitektur spesifik proyek yang sudah ada: ${rule_name}"
        else
            cp "$rule_file" "${TARGET_DIR}/.agents/rules/${rule_name}"
        fi
    fi
done

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
    "feedback"
    "revisions"
    "references"
    "references/ui"
    "references/features"
    "samples"
)

for sub in "${DOCS_SUBDIRS[@]}"; do
    mkdir -p "${TARGET_DIR}/docs/${sub}"
done

# Copy sample templates if available and not existing
if [ -d "${SOURCE_DIR}/docs/samples" ]; then
    for sample_file in "${SOURCE_DIR}/docs/samples/"*.md; do
        if [ -f "$sample_file" ]; then
            base_name="$(basename "$sample_file")"
            if [ ! -f "${TARGET_DIR}/docs/samples/${base_name}" ]; then
                cp "$sample_file" "${TARGET_DIR}/docs/samples/${base_name}"
            fi
        fi
    done
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
- `aod-progress-tracker` — Progress Tracker & Requirement Audit (output interactive checklist, terminal default / export dokumen)

**Phase 5 – Testing:**
- `aod-uat` — UAT Sheet Generator

**Maintenance & Revisions:**
- `aod-feedback-loop` — audit dokumen feedback/revisi, klasifikasi 3-Tier Scope (A/B/C), penegakan upstream-first, dan pembuatan laporan akhir.

**AOD Core Rules (Always Active):**
- Disiplin fase ketat: ikuti urutan Business Layer → System Design → UI Architecture → Development → Testing.
- Dependency chain mutlak: jangan membuat dokumen turunan tanpa dokumen prasyarat.
- AI berperan sebagai executor terkendali, bukan arsitek independen.
- Document versioning mutlak: seluruh dokumen di `docs/` wajib memiliki header semantic versioning (`vMAJOR.MINOR.PATCH`), tanggal `Last Updated`, dan tabel `Revision History`. AI wajib menaikkan versi (Major/Minor/Patch) setiap kali melakukan perubahan dokumen.
- Git feature-branching mutlak: seluruh implementasi pada Phase 4 wajib berada di branch terpisah (`phase/<num>-<slug>` atau `feat/<module>-<slug>`). Dilarang commit langsung ke `main`/`master`. Gunakan `smart-git-commit` untuk commit atomik.
- Grounding Context7 MCP mutlak: verifikasi dokumentasi resmi via Context7 (`resolve-library-id` & `query-docs`) sebelum menulis konfigurasi atau kode implementasi yang melibatkan library, framework, atau SDK pihak ketiga.
- Feedback & Upstream-First mutlak: seluruh dokumen revisi di `docs/feedback/` wajib diaudit via `aod-feedback-loop` dalam mode PLAN dan meminta klarifikasi user terlebih dahulu. AI dilarang langsung mengedit kode sebelum dokumen spesifikasi hulu diperbarui (SemVer bump). Setiap sesi revisi wajib menghasilkan `FINAL_REPORT_<name>.md`.
- Agent References Context (ARC) mutlak (Phase 3 & Phase 4): Setiap kali AI agent mengeksekusi step penulisan kode pada Phase 3 (UI Slicing: per halaman/komponen) dan Phase 4 (Development: per fitur/modul), AI WAJIB menghasilkan atau memperbarui dokumen referensi konteks (`docs/references/ui/REF-UI-<slug>.md` atau `docs/references/features/REF-FEAT-<module>-<slug>.md`) dan mendaftarkannya pada Master Registry (`docs/references/INDEX.md`). AI dilarang menandai task selesai, melewati DoD, atau melakukan commit kode tanpa menyertakan dokumen referensi dan update registry terkait.
- Bidirectional Reference Retrieval: Sebelum memulai penulisan atau refactoring kode pada modul/fitur yang sudah memiliki dokumen referensi, AI WAJIB membaca dokumen referensi terkait di `docs/references/` untuk menjaga kontinuitas arsitektur, props contract, business invariants, dan keputusan teknis sebelumnya.
- Design System Adherence mutlak: Seluruh pembuatan atau perubahan tampilan (UI, template, view, styling, komponen) pada Phase 3 (UI Slicing) maupun Phase 4 (Development) WAJIB tunduk 100% pada `docs/system-design/DESIGN_SYSTEM.md` dan `docs/system-design/UI_STYLE.md`. Dilarang mengimprovisasi token warna (hex sembarangan), ukuran font, grid spacing, atau komponen di luar spesifikasi Design System.
- Architecture Engineering Compliance mutlak (`always_on`): Seluruh implementasi kode pada Phase 4 (Development) WAJIB mematuhi aturan rekayasa arsitektur dinamis proyek yang didefinisikan pada `.agents/rules/aod-architecture-engineering.md` (dan `docs/development/ARCHITECTURE_ENGINEERING.md`) yang diturunkan dari `TECH_SPEC.md`. AI dilarang melanggar batasan layer, melakukan query di controller, atau memperkenalkan arsitektur liar di luar spesifikasi proyek.

### Design System Adherence Protocol

Protokol penegakan visual ini wajib dipatuhi setiap kali agent menulis atau mengubah kode tampilan:
1. **Token First:** Seluruh warna, tipografi, radius, bayangan, dan spacing harus memetakan ke design tokens resmi (`DESIGN_SYSTEM.md` & `UI_STYLE.md`).
2. **State Completeness:** Setiap komponen interaktif wajib mengimplementasikan state matrix lengkap: default, hover, active, focus-visible, disabled, loading, empty, dan error.
3. **Zero AI-Slop UI:** Dilarang menggunakan styling inline arbitrer (e.g. `style="color: #4a90e2"` atau `bg-[#123456]`). Jika token warna baru dibutuhkan, ajukan update ke `docs/system-design/DESIGN_SYSTEM.md` terlebih dahulu (upstream-first).

### Dynamic Architecture Engineering Protocol

Protokol aturan arsitektur dinamis proyek:
1. **Dynamic Rulebook Generation (Step 18):** Saat skill `aod-tech-spec` dijalankan, AI wajib mengekstrak aturan teknis proyek ke `.agents/rules/aod-architecture-engineering.md` dengan frontmatter `trigger: always_on` menggunakan template `docs/samples/ARCHITECTURE_ENGINEERING_TEMPLATE.md`, serta mencatat salinannya di `docs/development/ARCHITECTURE_ENGINEERING.md`.
2. **Always-On Context Awareness:** Aturan arsitektur ini aktif secara permanen di seluruh sesi. Agent WAJIB mematuhi batasan layer (thin controller, business logic di service layer, model hanya untuk relasi/invariants, FormRequest untuk validasi, Policy untuk otorisasi).
3. **Database & Concurrency Governance:** Seluruh operasi multi-tabel wajib dibungkus dalam `DB::transaction()`. Pengurangan inventori/saldo wajib menggunakan row locking (`lockForUpdate`).

### Agent References Context (ARC) Dynamic Protocol

Protokol dinamis ini wajib dijalankan oleh setiap AI Agent setiap kali berada di **Phase 3 (UI Slicing)** atau **Phase 4 (Development)**:

1. **Dynamic Discovery & Scope Detection:**
   - Tentukan fase aktif: Phase 3 (UI Slicing) atau Phase 4 (Feature Development).
   - Tentukan hierarki modul: Modul (`[module]`), Sub-modul (`[sub-module]`), dan Slug Fitur/Halaman (`[slug]`).
   - Periksa ketersediaan `docs/references/INDEX.md`. Jika belum ada, inisialisasi menggunakan template `docs/samples/MASTER_REFERENCE_INDEX_TEMPLATE.md`.
   - Jika dokumen referensi target (`REF-UI-*` atau `REF-FEAT-*`) sudah ada, baca terlebih dahulu sebelum mengedit kode.

2. **Standardized Reference Document Generation:**
   - **Phase 3 (UI Slicing):** Hasilkan/perbarui `docs/references/ui/REF-UI-<slug>.md` (ikuti `docs/samples/UI_REFERENCE_TEMPLATE.md`). Dokumentasikan: hierarki pohon komponen, tokens dari UI Style Doc, schema mock data, visual mapping state machine (loading, empty, error), props contract, dan panduan handoff integrasi backend Phase 4.
   - **Phase 4 (Feature Development):** Hasilkan/perbarui `docs/references/features/REF-FEAT-<module>-<slug>.md` (ikuti `docs/samples/FEATURE_REFERENCE_TEMPLATE.md`). Dokumentasikan: manifest file fisik (migration, model, DTO, service, controller, policy, test), alur lifecycle request, business invariants yang dijaga, pemetaan API contract, status transisi state machine, bukti test passing, dan panduan kontinuitas bagi agent berikutnya.

3. **Dynamic Master Registry Synchronization (`docs/references/INDEX.md`):**
   - Tambahkan/perbarui cabang pada **Module & Capability Hierarchy Tree**.
   - Tambahkan/perbarui baris pada tabel **Phase 3 UI Slicing Reference Registry** atau **Phase 4 Feature Development Reference Registry**.
   - Perbarui **Cross-Reference & Integration Matrix** ketika menghubungkan komponen UI dengan endpoint/service backend.
   - Naikkan versi SemVer pada header `docs/references/INDEX.md` dan perbarui tabel `Revision History`.

4. **DoD Gate 7 & Atomic Commit:**
   - Pastikan kriteria Pilar ke-7 (Knowledge Documentation & Context Continuity) pada `docs/development/DOD.md` terpenuhi.
   - Satukan file kode, dokumen referensi, dan `docs/references/INDEX.md` ke dalam satu atomic commit via `smart-git-commit`.
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
