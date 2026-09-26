<!-- antislop:start -->
## antislop
For UI, copy, people, mobile layout, or code comments work, load the antislop skill for the task:
- Core filter, always on: `antislop`
- UI / visual: `antislop-ui`
- Copy & text: `antislop-copywriting`
- Code comments: `antislop-code`
- Mobile / responsive: `antislop-layoutmobile`
- People: `antislop-human`
Before starting, ask the user when antislop applies: during the work, or after it is done.
<!-- antislop:end -->

<!-- aod:start -->
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
- `aod-quick-checklist` — Quick Terminal Checklist (tampilan checked list per-phase plan dan per-page UI slicing secara cepat via terminal)
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
<!-- aod:end -->




