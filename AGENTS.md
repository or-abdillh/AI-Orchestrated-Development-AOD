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
- Existing Project Initiation Exception: saat `aod-existing-project-initiation` dipakai, screening read-only dan dokumen _as-is_ boleh dibuat dari bukti repository tanpa memaksa rantai prasyarat scaffolding. Tandai fakta, inferensi, gap, dan konflik; dokumen _to-be_ tetap memerlukan keputusan/user input.
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

Dynamic project rules must fit the project's approved stack and architecture:

1. Treat `.agents/rules/aod-architecture-engineering.md` as a policy gate, not as approval for a proposed architecture.
2. Generate or replace project-specific `always_on` rules only from constraints marked **Approved** in `docs/development/TECH_SPEC.md`, using `docs/samples/ARCHITECTURE_ENGINEERING_TEMPLATE.md`. Keep the documentation mirror in `docs/development/ARCHITECTURE_ENGINEERING.md` synchronized.
3. Keep recommendations, examples, assumptions, and open decisions out of active rules. For an unapproved Tech Spec, do not activate proposed project-specific rules.
4. Do not impose framework-specific patterns or database mechanisms universally. Use the project's verified stack, approved Technical Specification, and upstream business/interface contracts.
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
   <!-- aod:end -->
