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

# Update AOD-managed rules while preserving project-specific architecture rules.
for rule_file in "${SOURCE_DIR}/.agents/rules/"*; do
    if [ -f "$rule_file" ]; then
        rule_name="$(basename "$rule_file")"
        if [ "$rule_name" = "aod-architecture-engineering.md" ] && [ -f "${TARGET_DIR}/.agents/rules/${rule_name}" ]; then
            log_info "Mempertahankan aturan arsitektur spesifik proyek: ${rule_name}"
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
log_ok "Seluruh aturan (rules), 28 native AOD skills, dan skill pelengkap berhasil dipasang."

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

# 4. Inject AOD guidance into common agent instruction files
log_step "Mengonfigurasi instruksi agen (AGENTS, Gemini, Claude, Cursor, Copilot, Windsurf)..."

AOD_CONFIG_BLOCK='<!-- aod:start -->
## AI-Orchestrated Development (AOD)

Untuk memulai atau melanjutkan project dengan metodologi AOD, aktifkan skill yang sesuai:

**Entry Point (Mulai di sini):**
- `aod-orchestrator` — panduan interaktif lengkap fase demi fase, dari discovery hingga UAT.
- `aod-existing-project-initiation` — screening codebase existing, deteksi tech stack, pemetaan domain berbasis bukti, dan pemilihan dokumen AOD yang relevan.

**Optional Commercial Proposal (setelah PRD & Tech Spec disetujui):**
- `aod-proposal` — proposal client-ready setelah PRD dan Tech Spec stabil; pisahkan effort/durasi dan tandai harga TBD jika dasar biaya tidak tersedia.

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
- `aod-api-contract` — API, Web Route, atau mixed contract sesuai Tech Spec dan konfirmasi developer
- `aod-ui-flow` — UI Flow / Screen Map
- `aod-website-concept` — Website Concept Document
- `aod-design-system` — framework-neutral visual and interaction rules
- `aod-ui-style` — canonical framework-neutral visual tokens

**Phase 3 – UI Architecture:**
- `aod-ui-component-map` — UI Component Map
- `aod-ui-slicing` — Full UI Slicing Document

**Phase 4 – Development:**
- `aod-tech-spec` — Technical Specification
- `aod-phase-plan` — Development Phase Plan
- `aod-feature-prompts` — Feature Prompt Library
- `aod-tailwind-config` — optional Phase 4 adapter for the approved styling framework/version; Tailwind only when the project uses it
- `aod-page-slicer` — Implement one approved UI page with mock data and ARC
- `aod-dod` — Definition of Done Checklist
- `aod-quick-checklist` — Quick Terminal Checklist (tampilan checked list per-phase plan dan per-page UI slicing secara cepat via terminal)
- `aod-progress-tracker` — Progress Tracker & Requirement Audit (output interactive checklist, terminal default / export dokumen)

**Phase 5 – Testing:**
- `aod-uat` — UAT Sheet Generator

**Maintenance & Revisions:**
- `aod-feedback-loop` — audit dampak feedback/revisi, pembaruan upstream-first, eksekusi terotorisasi, dan pelaporan hasil aktual.

**AOD Core Rules (Always Active):**
- Disiplin fase ketat: ikuti urutan Business Layer → System Design → UI Architecture → Development → Testing.
- Dependency chain mutlak: jangan membuat dokumen turunan tanpa dokumen prasyarat.
- Existing Project Initiation Exception: saat `aod-existing-project-initiation` dipakai, screening read-only dan dokumen *as-is* boleh dibuat dari bukti repository tanpa memaksa rantai prasyarat scaffolding. Tandai fakta, inferensi, gap, dan konflik; dokumen *to-be* tetap memerlukan keputusan/user input.
- AI berperan sebagai executor terkendali, bukan arsitek independen.
- Document versioning mutlak: seluruh dokumen di `docs/` wajib memiliki header semantic versioning (`vMAJOR.MINOR.PATCH`), tanggal `Last Updated`, dan tabel `Revision History`. AI wajib menaikkan versi (Major/Minor/Patch) setiap kali melakukan perubahan dokumen.
- Git feature-branching mutlak: seluruh implementasi pada Phase 4 wajib berada di branch terpisah (`phase/<num>-<slug>` atau `feat/<module>-<slug>`). Dilarang commit langsung ke `main`/`master`. Gunakan `smart-git-commit` untuk commit atomik.
- Grounding Context7 MCP mutlak: verifikasi dokumentasi resmi via Context7 (`resolve-library-id` & `query-docs`) sebelum menulis konfigurasi atau kode implementasi yang melibatkan library, framework, atau SDK pihak ketiga.
- Feedback & Upstream-First mutlak: audit feedback melalui `aod-feedback-loop` dan perbarui dokumen hulu yang terdampak sebelum implementasi. Klarifikasi hanya keputusan material yang belum jelas; jika pengguna sudah meminta perubahan, jangan meminta persetujuan ulang. Buat `FINAL_REPORT_<name>.md` setelah eksekusi bila diwajibkan workflow proyek atau diminta pengguna.
- Agent References Context (ARC) mutlak pada implementasi Phase 4: setiap halaman yang diimplementasikan via `aod-page-slicer` wajib memiliki UI reference (`docs/references/ui/REF-UI-<slug>.md`); setiap fitur backend wajib memiliki feature reference (`docs/references/features/REF-FEAT-<module>-<slug>.md`). Daftarkan masing-masing pada Master Registry (`docs/references/INDEX.md`) dan baca referensi yang sudah ada sebelum mengubah implementasi. Phase 3 menghasilkan dokumen rancangan, bukan kode halaman.
- Bidirectional Reference Retrieval: Sebelum memulai penulisan atau refactoring kode pada modul/fitur yang sudah memiliki dokumen referensi, AI WAJIB membaca dokumen referensi terkait di `docs/references/` untuk menjaga kontinuitas arsitektur, props contract, business invariants, dan keputusan teknis sebelumnya.
- Design System Adherence: gunakan `DESIGN_SYSTEM.md` untuk prinsip, komponen, state, dan aksesibilitas; gunakan `UI_STYLE.md` sebagai sumber token visual. Keduanya framework-neutral. Petakan token ke framework hanya setelah Tech Spec memilih stack; jangan mengasumsikan Tailwind.
- Architecture Engineering Compliance mutlak (`always_on`): Seluruh implementasi kode pada Phase 4 (Development) WAJIB mematuhi aturan rekayasa arsitektur dinamis proyek yang didefinisikan pada `.agents/rules/aod-architecture-engineering.md` (dan `docs/development/ARCHITECTURE_ENGINEERING.md`) yang diturunkan dari `TECH_SPEC.md`. AI dilarang melanggar batasan layer, melakukan query di controller, atau memperkenalkan arsitektur liar di luar spesifikasi proyek.

### Design System Adherence Protocol

Protokol ini wajib dipatuhi saat merancang spesifikasi UI di Phase 3 dan menulis atau mengubah kode tampilan di Phase 4:
1. **Token First:** Seluruh warna, tipografi, radius, bayangan, dan spacing harus memetakan ke design tokens resmi (`DESIGN_SYSTEM.md` & `UI_STYLE.md`).
2. **State Completeness:** Setiap komponen interaktif wajib mengimplementasikan state matrix lengkap: default, hover, active, focus-visible, disabled, loading, empty, dan error.
3. **Zero AI-Slop UI:** Dilarang menggunakan styling inline arbitrer (e.g. `style="color: #4a90e2"` atau `bg-[#123456]`). Jika token warna baru dibutuhkan, ajukan update ke `docs/system-design/DESIGN_SYSTEM.md` terlebih dahulu (upstream-first).

### Dynamic Architecture Engineering Protocol

Dynamic project rules must fit the approved project stack and architecture:
1. Treat `.agents/rules/aod-architecture-engineering.md` as a policy gate, not as approval for a proposed architecture.
2. Generate or replace project-specific `always_on` rules only from constraints marked **Approved** in `docs/development/TECH_SPEC.md`, using `docs/samples/ARCHITECTURE_ENGINEERING_TEMPLATE.md`. Keep the documentation mirror in `docs/development/ARCHITECTURE_ENGINEERING.md` synchronized.
3. Keep recommendations, examples, assumptions, and open decisions out of active rules. For an unapproved Tech Spec, do not activate proposed project-specific rules.
4. Do not impose framework-specific patterns or database mechanisms universally. Use the verified project stack, approved Technical Specification, and upstream business/interface contracts.
5. When active rules conflict with an approved Tech Spec, report the conflict and pause only the affected implementation until it is resolved. Preserve unrelated local rules.

### Agent References Context (ARC) Dynamic Protocol

Terapkan protokol ini saat menulis atau mengubah kode pada Phase 4. Phase 3 menghasilkan dokumen rancangan UI, bukan kode halaman.

1. **Dynamic Discovery & Scope Detection:**
   - Tentukan apakah task adalah implementasi halaman UI atau fitur backend dan identifikasi module, screen/feature slug.
   - Tentukan hierarki modul: Modul (`[module]`), Sub-modul (`[sub-module]`), dan Slug Fitur/Halaman (`[slug]`).
   - Periksa ketersediaan `docs/references/INDEX.md`. Jika belum ada, inisialisasi menggunakan template `docs/samples/MASTER_REFERENCE_INDEX_TEMPLATE.md`.
   - Jika dokumen referensi target (`REF-UI-*` atau `REF-FEAT-*`) sudah ada, baca terlebih dahulu sebelum mengedit kode.

2. **Standardized Reference Document Generation:**
   - **UI page (`aod-page-slicer`):** Hasilkan/perbarui `docs/references/ui/REF-UI-<slug>.md` (template `docs/samples/UI_REFERENCE_TEMPLATE.md`) berisi screen ID, route, file aktual, komponen, tokens, mock/data contract, state, handoff integrasi, dan bukti verifikasi.
   - **Backend feature:** Hasilkan/perbarui `docs/references/features/REF-FEAT-<module>-<slug>.md` (template `docs/samples/FEATURE_REFERENCE_TEMPLATE.md`) berisi manifest file aktual, lifecycle, invariants, contract mapping, dan bukti verifikasi yang tersedia.

3. **Dynamic Master Registry Synchronization (`docs/references/INDEX.md`):**
   - Tambahkan/perbarui cabang pada **Module & Capability Hierarchy Tree**.
   - Tambahkan/perbarui baris pada **UI Page Implementation Reference Registry** atau **Phase 4 Feature Development Reference Registry**.
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

# Other coding agents receive concise pointers to the canonical AOD guidance.
# Marked blocks are replaced on reinstall; all content outside them is preserved.
inject_pointer() {
    local target_file="$1"
    local block="$2"
    mkdir -p "$(dirname "$target_file")"
    if [ ! -f "$target_file" ]; then
        printf '%s\n' "$block" > "$target_file"
        log_ok "Membuat instruksi agen: ${target_file}"
    elif grep -q '<!-- aod:start -->' "$target_file"; then
        TARGET_FILE="$target_file" AOD_BLOCK="$block" node -e '
            const fs = require("fs");
            const file = process.env.TARGET_FILE;
            const block = process.env.AOD_BLOCK;
            const content = fs.readFileSync(file, "utf8");
            fs.writeFileSync(file, content.replace(/<!-- aod:start -->[\s\S]*?<!-- aod:end -->/m, block), "utf8");
        '
        log_ok "Memperbarui instruksi AOD: ${target_file}"
    else
        printf '\n\n%s\n' "$block" >> "$target_file"
        log_ok "Menambahkan instruksi AOD: ${target_file}"
    fi
}

CLAUDE_BLOCK='<!-- aod:start -->
# AOD project guidance
Read `AGENTS.md` before planning or changing this project. Follow its AOD phase gates, approved Tech Spec, project architecture rules, UI tokens, and ARC references. Use the relevant `.agents/skills/aod-*` skill; do not assume a framework or route style that the approved project documents have not selected.
<!-- aod:end -->'
COPILOT_BLOCK='<!-- aod:start -->
# AOD project guidance
Read `AGENTS.md` for the canonical AOD workflow and project constraints before planning or editing. Follow approved Tech Spec and architecture rules, use the relevant `.agents/skills/aod-*` skill, and preserve project files outside AOD-managed paths. Do not assume a framework, API, or styling system that project evidence has not selected.
<!-- aod:end -->'
CURSOR_BLOCK=$'---\ndescription: AOD project workflow and implementation constraints\nalwaysApply: true\n---\n<!-- aod:start -->\nRead `AGENTS.md` for canonical AOD instructions before planning or editing. Follow approved Tech Spec, architecture rules, UI tokens, and ARC references. Use the relevant `.agents/skills/aod-*` skill; do not assume an unapproved framework or route style.\n<!-- aod:end -->'
WINDSURF_BLOCK='<!-- aod:start -->
# AOD project guidance
Read `AGENTS.md` before planning or editing. Follow approved AOD phase gates, Tech Spec, architecture rules, UI tokens, and ARC references. Use the relevant `.agents/skills/aod-*` skill and avoid assumptions unsupported by project documents.
<!-- aod:end -->'
inject_pointer "${TARGET_DIR}/CLAUDE.md" "$CLAUDE_BLOCK"
inject_pointer "${TARGET_DIR}/.github/copilot-instructions.md" "$COPILOT_BLOCK"
inject_pointer "${TARGET_DIR}/.cursor/rules/aod.mdc" "$CURSOR_BLOCK"
inject_pointer "${TARGET_DIR}/.windsurfrules" "$WINDSURF_BLOCK"

echo ""
echo -e "${C_GREEN}${C_BOLD}🎉 Instalasi AOD Framework Berhasil!${C_RESET}\n"
echo -e "Untuk mulai menjalankan AOD pada AI coding agent Anda:"
echo -e " 1. Buka coding agent pilihan Anda (Codex, Claude, Gemini, Cursor, Copilot, Windsurf, atau Antigravity)."
echo -e " 2. Untuk proyek baru, ketik ${C_BOLD}\"Mulai AOD\"${C_RESET}; untuk codebase existing, ketik ${C_BOLD}\"Audit codebase ini untuk adopsi AOD\"${C_RESET}."
echo -e " 3. AI akan membaca panduan fase atau melakukan screening codebase sebelum menyarankan dokumen."
echo ""
echo -e "Maintainer: ${C_BOLD}Oka R. Abdillah${C_RESET} | Software Engineer"
echo -e "GitHub: @or-abdillh | Instagram: or.abdillh"
