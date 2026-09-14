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

**Phase 5 – Testing:**
- `aod-uat` — UAT Sheet Generator

**AOD Core Rules (Always Active):**
- Disiplin fase ketat: ikuti urutan Business Layer → System Design → UI Architecture → Development → Testing.
- Dependency chain mutlak: jangan membuat dokumen turunan tanpa dokumen prasyarat.
- AI berperan sebagai executor terkendali, bukan arsitek independen.
- Document versioning mutlak: seluruh dokumen di `docs/` wajib memiliki header semantic versioning (`vMAJOR.MINOR.PATCH`), tanggal `Last Updated`, dan tabel `Revision History`. AI wajib menaikkan versi (Major/Minor/Patch) setiap kali melakukan perubahan dokumen.
- Git feature-branching mutlak: seluruh implementasi pada Phase 4 wajib berada di branch terpisah (`phase/<num>-<slug>` atau `feat/<module>-<slug>`). Dilarang commit langsung ke `main`/`master`. Gunakan `smart-git-commit` untuk commit atomik.
- Grounding Context7 MCP mutlak: verifikasi dokumentasi resmi via Context7 (`resolve-library-id` & `query-docs`) sebelum menulis konfigurasi atau kode implementasi yang melibatkan library, framework, atau SDK pihak ketiga.
<!-- aod:end -->




