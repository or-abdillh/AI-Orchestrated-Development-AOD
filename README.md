# AI-Orchestrated Development (AOD) Framework

[![Framework](https://img.shields.io/badge/Methodology-AOD%20Framework-blue.svg)](#overview)
[![Agentic Skills](https://img.shields.io/badge/Native%20Skills-28%20Skills-emerald.svg)](#-skills-inventory--phase-mapping)
[![Compatibility](https://img.shields.io/badge/Agent-Antigravity%20%7C%20Gemini%20%7C%20Claude%20%7C%20Copilot-purple.svg)](#-how-to-use-in-real-projects)
[![License](https://img.shields.io/badge/License-MIT-gray.svg)](LICENSE)

> **"AI executes. Architect decides. Structure governs."**
>
> Metodologi pengembangan perangkat lunak dan ekosistem _agentic skills_ untuk mentransformasi AI dari autopilot tanpa kendali menjadi **implementation accelerator yang disiplin, terstruktur, dan patuh arsitektur**.

---

## 📑 Daftar Isi

- [Quick Install (One-Liner)](#-quick-install-one-liner)
- [Overview](#-overview)
- [Mengapa AOD Dibutuhkan?](#-mengapa-aod-dibutuhkan)
- [Prinsip Fundamental](#-5-prinsip-fundamental)
- [Alur Kerja (End-to-End Workflow)](#-alur-kerja-end-to-end-workflow)
- [Skills Inventory & Phase Mapping](#-skills-inventory--phase-mapping)
- [Guardrails & Rules Enforcement](#-guardrails--rules-enforcement)
- [Panduan Penggunaan di Real Project](#-panduan-penggunaan-di-real-project)
- [Struktur Output Dokumen](#-struktur-output-dokumen)
- [Skill Ekosistem Pelengkap](#-skill-ekosistem-pelengkap)
- [Author & Maintainer](#-author--maintainer)
- [Lisensi](#-lisensi)

---

## ⚡ Quick Install (One-Liner)

Pasang seluruh ekosistem AOD Framework (28 native AOD skills, 5 Rules, skill pelengkap, AGENTS.md, registry, helper checkpoint, dan template `docs/samples/`) ke dalam project apa pun (proyek baru maupun proyek yang sudah berjalan seperti Laravel, Next.js, Vue, Django, dsb.) dengan **satu baris perintah**:

```bash
curl -fsSL https://raw.githubusercontent.com/or-abdillh/AI-Orchestrated-Development-AOD/main/install.sh | bash
```

> **Atau tentukan direktori target secara spesifik:**
>
> ```bash
> curl -fsSL https://raw.githubusercontent.com/or-abdillh/AI-Orchestrated-Development-AOD/main/install.sh | bash -s -- /path/to/your/project
> ```

---

## 💡 Overview

**AI-Orchestrated Development (AOD)** adalah framework yang dirancang khusus untuk pengembang mandiri (_solo developers_), konsultan teknis, dan tim freelance yang membangun sistem skala SME (_Small-Medium Enterprise_).

AOD menjaga keputusan produk, kontrak dan implementasi tetap konsisten dengan
workflow yang mengikuti jenis pekerjaan.

### Pilih jalur pekerjaan

| Kebutuhan | Jalur | Interaksi developer |
| --- | --- | --- |
| Proyek baru / discovery | Guided Phase 0–5 | Review keputusan dan mode fase sesuai kebutuhan |
| Adopsi proyek existing | Screening baseline terarah | Pilih scope, pertahankan pekerjaan yang valid |
| Bug, perubahan fitur, modul baru | Scoped change | Satu rencana mencakup dokumen, kode, checks dan dokumentasi hasil |

Penambahan modul pada produk existing tidak memulai ulang Phase 1–5.
Untuk permintaan plan-then-wait, agent mengajukan satu rencana gabungan lalu
menunggu. Setelah rencana disetujui, agent menjalankan seluruh scope tanpa
approval per dokumen atau fase. Permintaan apply yang sudah jelas langsung
mengotorisasi scope tersebut. Pertanyaan tambahan hanya untuk keputusan
material baru, konflik atau tindakan di luar otorisasi.

### Contoh workflow perubahan

> Developer: “Rencanakan penambahan field equipment serial number, tunggu approval.”
> Agent: menjelaskan delta Data Dictionary/interface yang relevan, migration,
> validasi, UI dan pengujian; tidak merevisi BRD atau Design System.
> Developer: “Setuju, implementasikan.”
> Agent: memperbarui kontrak esensial → implementasi → checks → ARC/dokumentasi
> aktual → laporan hasil. Tidak meminta ulang persetujuan versi dokumen.

Bug yang mengembalikan perilaku sesuai spesifikasi tidak wajib mengubah PRD.
Kontrak data/permission/interface/state yang benar-benar berubah dicatat sebelum
kode terkait. Detail implementasi dan hasil checks dicatat sesudah verifikasi.
Dokumentasi yang diwajibkan tetap menjadi syarat pekerjaan selesai.

### Resume, mode dan checkpoint

Gunakan **Mulai AOD**, **Lanjut AOD / lanjut**, **Status AOD**, **Jeda AOD**,
dan **Ubah mode AOD**. Agent memilih profile sebelum menjalankan scheduler.
Pada perubahan fitur, default adalah eksekusi sampai selesai dalam scope;
mode bertahap tersedia ketika dipilih developer. Preferensi paralelisme sesi
bisa dipakai ulang. Question box memakai fallback chat bernomor bila tidak
tersedia; pertanyaan material yang belum dijawab tidak dianggap disetujui.

Checkpoint guided tetap di `docs/aod/WORKFLOW_STATE.json`; perubahan terpisah
bisa memakai `docs/aod/changes/<id>.json` tanpa membuka ulang baseline. Source
hash yang berubah memicu penilaian dampak: metadata/editorial tidak otomatis
membatalkan keputusan bisnis. Helpers tidak memahami semantik dokumen secara
otomatis; agent harus membaca diff dan mencatat bukti penilaiannya.

### Instalasi ulang dan coding agent

Installer memperbarui file milik paket dan blok AOD pada instruksi agent.
File custom, dokumen produk, checkpoint termasuk `docs/aod/changes/`, isi di
luar blok AOD, dan aturan arsitektur spesifik proyek tetap dipertahankan.
`AGENTS.md` menjadi panduan lintas agent; installer juga menyiapkan Gemini,
Claude, Copilot, Cursor dan Windsurf. Ketersediaan widget dan sub-agent
mengikuti kemampuan platform, bukan jaminan dari skill pack.

### Peta guided discovery (generated)

Peta ini untuk discovery dan phased review; perubahan fitur menggunakan
contracts → implementation → verification → documentation lintas domain.

<!-- aod:map:start -->
| Phase | Steps / executing skills |
| --- | --- |
| 0 — Discovery / Baseline | `discovery`, `aod-existing-project-initiation` |
| 1 — Business Layer | `aod-brd`, `aod-business-flow`, `aod-prd`, `aod-flowchart`, `aod-rbac`, `aod-data-dictionary`, `aod-dbml` |
| 2 — System Design | `aod-state-machine`, `aod-api-contract`, `aod-ui-flow`, `aod-website-concept`, `aod-design-system`, `aod-ui-style` |
| 3 — UI Architecture | `aod-ui-component-map`, `aod-ui-slicing` |
| 4 — Development | `aod-tech-spec`, `aod-phase-plan`, `aod-feature-prompts`, `aod-dod`, `aod-tailwind-config`, `implementation` |
| 5 — Testing | `aod-uat` |
<!-- aod:map:end -->

Workflow completion, implementasi requirement, hasil verifikasi, dan UAT
execution/acceptance dilaporkan terpisah. Dokumen lengkap tidak berarti produk
selesai. Fase/release pada Phase Plan bukan fase metodologi AOD.

## 🛠️ Skills Inventory & Phase Mapping

Repository ini dilengkapi dengan **28 native AOD skills** serta skill pelengkap yang tersimpan di [`.agents/skills/`](.agents/skills/):

### Entry Point & Optional Commercial Proposal

| Skill                                 | Command Trigger                                                                                         | Input Dokumen                                                           | Output Artefak                                                                 |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **`aod-orchestrator`**                | `"start AOD"`, `"mulai AOD"`, `"panduan AOD"`                                                           | _None (Interactive)_                                                    | Eksekusi workflow dan checkpoint persisten                                                    |
| **`aod-existing-project-initiation`** | `"initiate existing project"`, `"adopsi AOD pada proyek existing"`, `"audit codebase untuk phase plan"` | Repository yang sudah berjalan                                          | Laporan screening di chat; dokumen AOD pilihan user berdasarkan bukti codebase |
| **`aod-proposal`**                    | `"buat proposal"`, `"project quotation"`                                                                | Approved, stable PRD and Tech Spec; Phase Plan/rate card when available | Scope-based proposal and estimate in `docs/proposal/PROPOSAL.md`               |

### Phase 1 — Business Layer

| Skill                     | Persona                     | Input Wajib        | Output Artefak                     |
| ------------------------- | --------------------------- | ------------------ | ---------------------------------- |
| **`aod-brd`**             | Enterprise Business Analyst | Study Case         | `docs/business/BRD.md`             |
| **`aod-business-flow`**   | Business Process Architect  | Study Case         | `docs/business/BUSINESS_FLOW.md`   |
| **`aod-prd`**             | Senior Product Manager      | BRD, Business Flow | `docs/business/PRD.md`             |
| **`aod-flowchart`**       | BPA & System Architect      | Business Flow      | `docs/business/FLOWCHART.md`       |
| **`aod-rbac`**            | Access Control Architect    | PRD                | `docs/business/RBAC.md`            |
| **`aod-data-dictionary`** | Senior Data Architect       | PRD                | `docs/business/DATA_DICTIONARY.md` |
| **`aod-dbml`**            | Database Designer           | Data Dictionary    | `docs/business/SCHEMA.dbml`        |

### Phase 2 — System Design

| Skill                     | Persona                         | Input Wajib                                                                          | Output Artefak                                                   |
| ------------------------- | ------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **`aod-state-machine`**   | DDD Specialist                  | Business Flow (TO-BE), PRD                                                           | `docs/system-design/STATE_MACHINE.md`                            |
| **`aod-api-contract`**    | Application Interface Architect | PRD, Data Dictionary, Tech Spec (when available) + developer route-mode confirmation | `docs/system-design/API_CONTRACT.md` (API, web routes, or mixed) |
| **`aod-ui-flow`**         | Enterprise UX Designer          | PRD, Business Flow                                                                   | `docs/system-design/UI_FLOW.md`                                  |
| **`aod-website-concept`** | Senior UX Strategist            | Study Case, BRD, Flow                                                                | `docs/system-design/WEBSITE_CONCEPT.md`                          |
| **`aod-design-system`**   | Design System Architect         | Website Concept Doc                                                                  | `docs/system-design/DESIGN_SYSTEM.md`                            |
| **`aod-ui-style`**        | Senior UI Designer              | Website Concept, Design System                                                       | `docs/system-design/UI_STYLE.md`                                 |

### Phase 3 — UI Architecture

| Skill                      | Persona            | Input Wajib              | Output Artefak                          |
| -------------------------- | ------------------ | ------------------------ | --------------------------------------- |
| **`aod-ui-component-map`** | Frontend Architect | UI Flow, Design System   | `docs/ui-architecture/COMPONENT_MAP.md` |
| **`aod-ui-slicing`**       | UI Engineer        | Component Map, Style Doc | `docs/ui-architecture/UI_SLICING.md`    |

### Phase 4 — Development & Tracking

| Skill                      | Persona                   | Input Wajib                                                  | Output Artefak                                                            |
| -------------------------- | ------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------- |
| **`aod-tech-spec`**        | Solution Architect        | Approved product/system inputs or existing-project evidence  | `docs/development/TECH_SPEC.md`; approved project rules when selected     |
| **`aod-phase-plan`**       | Technical Project Manager | Technical Specification                                      | `docs/development/PHASE_PLAN.md`                                          |
| **`aod-feature-prompts`**  | AI Development Strategist | Tech Spec, Phase Plan                                        | `docs/development/FEATURE_PROMPTS.md`                                     |
| **`aod-dod`**              | Software Quality Auditor  | Tech Spec, Feature Prompts                                   | `docs/development/DOD.md`                                                 |
| **`aod-tailwind-config`**  | Framework Token Adapter   | UI Style, approved Tech Spec and Phase Plan                  | Project styling config + `docs/ui-architecture/DESIGN_TOKENS.md`          |
| **`aod-page-slicer`**      | Frontend Engineer         | Approved Tech Spec, Phase Plan, UI contracts                 | Page code, mock fixtures, UI reference                                    |
| **`aod-quick-checklist`**  | Delivery Snapshot         | Phase Plan and/or UI Slicing                                 | Compact read-only status and next action in chat/terminal                 |
| **`aod-progress-tracker`** | Requirement Audit Lead    | Available requirements, plan, code and verification evidence | Detailed traceability audit in chat; `PROGRESS_REPORT.md` only on request |

### Phase 5 — Testing

| Skill         | Persona                    | Input Wajib                                                        | Output Artefak                                                            |
| ------------- | -------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| **`aod-uat`** | QA Lead & Product Delivery | Approved requirements; relevant Flow, RBAC, State Machine, UI Flow | Requirement/role/state traceable scenarios in `docs/testing/UAT_SHEET.md` |

### Maintenance & Revisions

| Skill                   | Persona                       | Input Wajib                          | Output Artefak                         |
| ----------------------- | ----------------------------- | ------------------------------------ | -------------------------------------- |
| **`aod-feedback-loop`** | Lead Architect & Delivery Mgr | Feedback, change request, atau instruksi langsung | Perubahan terarah dan ringkasan; laporan file bila diperlukan |

---

## 🛡️ Guardrails & Rules Enforcement

Sistem AOD dilindungi oleh file aturan otomatis yang selalu aktif di [`.agents/rules/`](.agents/rules/):

1. **`aod-core.md` (Always Active):**
   - Menjaga dependency dan memilih jalur guided atau scoped change sesuai task.
   - Meminta klarifikasi hanya pada keputusan material; memakai baseline dan rencana delta untuk perubahan terarah.
   - Menggunakan otoritas masing-masing domain dan meminta keputusan untuk konflik material, tanpa ranking universal.
2. **`aod-coding-standards.md` (Development Phase):**
   - **Framework-Agnostic:** Mendukung Laravel, NestJS, Django, Next.js, FastAPI, Go, dll.
   - Mengikuti batas layer yang disetujui pada Tech Spec proyek.
   - Menangani masalah query sesuai ORM, data dan kebutuhan kinerja proyek.
   - Validasi dan otorisasi mengikuti framework serta kontrak proyek.
3. **`aod-document-versioning.md` (Document Lifecycle & Semantic Tracking):**
   - **Header Wajib:** Dokumen Markdown AOD yang dikelola di `docs/` wajib diawali dengan metadata versi semantic (`vMAJOR.MINOR.PATCH`), tanggal `Last Updated`, status dokumen, dan tabel `Revision History`.
   - **Version Bumping:** Naikkan versi sekali per perubahan koheren; state JSON memakai schema/revision metadata.
   - **Audit Trail Terjamin:** Setiap perubahan terdokumentasi rapi seiring berjalannya proyek.
4. **Git Feature-Branching Enforcement (Phase 4 Development):**
   - **Dilarang Direct Commit ke Main:** Semua eksekusi kode fitur wajib berada di branch terpisah.
   - **Konvensi Branch:** `phase/<num>-<phase-slug>` untuk branch fase, dan `feat/<module>-<feature-slug>` untuk branch per-fitur.
   - **Alur Atomik:** `Checkout branch -> Koding tugas 1-8 -> Validasi DoD -> Atomic commit (smart-git-commit) -> Merge/PR`.
   - **Skill Terintegrasi:** Didukung oleh `git-flow-branch-creator`, `git-workflow-and-versioning`, dan `smart-git-commit`.
5. **Context7 MCP Source-Driven Grounding (Official Docs Verification):**
   - **No Hallucinated APIs:** AI dilarang mengarang sintaks atau konfigurasi library pihak ketiga.
   - **Verifikasi:** Gunakan Context7 bila tersedia, atau dokumentasi resmi yang cocok dengan versi stack proyek.
6. **`aod-feedback-and-revisions.md` (Feedback Loop & Upstream-First Rule):**
   - **Planning and Authorization:** Audit-only requests menghasilkan rencana tanpa mengubah file. Jika user secara eksplisit meminta implementasi, kerjakan bagian yang jelas tanpa meminta persetujuan ulang; klarifikasi hanya keputusan material yang belum terselesaikan.
   - **3-Tier Scope Classification:** Memetakan butir revisi ke **Scope A (Doc Only)**, **Scope B (Feature Modification)**, atau **Scope C (New Feature / Scope Expansion)**.
   - **Upstream Cascading:** Patch kontrak esensial terdampak sebelum kode terkait; sinkronkan fakta implementasi sesudah checks. Rencana yang disetujui mengotorisasi keduanya tanpa approval berulang.
   - **Factual Reporting:** Buat laporan eksekusi setelah perubahan bila diwajibkan workflow proyek atau diminta user; jangan menyebut pekerjaan audit-only sebagai eksekusi selesai.
7. **Requirement Traceability & Progress Tracking (`aod-progress-tracker`):**
   - **Full Requirement Traceability:** Memetakan requirement dan work item ke rencana, implementasi, DoD/ARC, serta bukti verifikasi yang tersedia.
   - **Evidence-Based Status:** Membedakan completed/verified, implemented/unverified, in progress, planned, blocked, drift, dan unknown. Git menjadi bukti opsional, bukan prasyarat.
   - **Dual Output Modes:** Ringkasan audit tampil di chat secara default; laporan `docs/development/PROGRESS_REPORT.md` dibuat hanya saat diminta.
8. **Rapid Terminal Checklists (`aod-quick-checklist`):**
   - **Compact and Read-Only:** Menampilkan status singkat tanpa membuat file atau menjalankan tests.
   - **Scope-Specific:** Merangkum Phase Plan, status rencana/implementasi halaman UI, atau keduanya; tidak menggantikan audit traceability lengkap.
   - **One Next Action:** Menunjukkan satu langkah dependency-ready berdasarkan plan yang tersedia.
9. **Stakeholder UAT (`aod-uat`):**
   - Menautkan setiap skenario ke requirement/acceptance ID, actor role, state awal/akhir jika relevan, dan expected result yang bisa diamati.
   - Menyediakan coverage matrix dan ruang pencatatan hasil/sign-off; tidak menyatakan UAT lulus sebelum stakeholder menjalankannya.

```markdown
<!-- Contoh Header Metadata pada Setiap Dokumen docs/ -->

# Product Requirement Document (PRD)

> **Version:** `v1.2.0`  
> **Last Updated:** `2026-09-14`  
> **Status:** `Approved`  
> **Author / Generator:** `aod-prd`

---

### Revision History

| Version  | Date       | Author  | Description of Changes                                       |
| -------- | ---------- | ------- | ------------------------------------------------------------ |
| `v1.0.0` | 2026-09-10 | aod-prd | Initial draft from BRD & Business Flow.                      |
| `v1.1.0` | 2026-09-12 | aod-prd | Added Payment Gateway integration requirements.              |
| `v1.2.0` | 2026-09-14 | aod-prd | Added multi-currency support and localized tax calculations. |
```

---

## 🚀 Panduan Penggunaan di Real Project

### 1. Inisialisasi Proyek Baru

Panggil orchestrator untuk memeriksa kelengkapan awal dokumen proyek Anda:

```text
User: "Mulai proyek baru dengan AOD."
Agent: Mengaktifkan aod-orchestrator, menanyakan ketersediaan Study Case / Business Discovery.
```

### 2. Inisialisasi Proyek Existing

Untuk codebase yang sudah memiliki modul dan fitur berjalan, mulai dengan skill screening khusus. Skill akan mendeteksi stack dari manifest, memetakan domain dari bukti implementasi, lalu menampilkan pilihan dokumen yang relevan. Dokumen baru dibuat setelah Anda memilihnya:

```text
User: "Audit codebase ini untuk adopsi AOD dan susun opsi phase plan."
Agent: Menjalankan aod-existing-project-initiation, memeriksa stack dan codebase secara read-only, lalu meminta pilihan dokumen berdasarkan hasil audit.
```

### 3. Membangun Dokumen Bisnis (Phase 1)

Jalankan pembentukan BRD dan Business Flow:

```text
User: "Generate BRD dari study case ini: [paste ringkasan bisnis]"
Agent: Menjalankan aod-brd -> menghasilkan docs/business/BRD.md

User: "Lanjut buat Business Flow dan PRD."
Agent: Menjalankan aod-business-flow -> aod-prd.
```

### 4. Merancang Sistem & Data (Phase 1 & 2)

Generate kamus data dan kontrak antarmuka:

```text
User: "Buat data dictionary dan skema DBML."
Agent: Menjalankan aod-data-dictionary dan aod-dbml.

User: "Rancang API contract dan UI flow."
Agent: Menjalankan aod-api-contract dan aod-ui-flow secara terpadu.
```

### 5. Eksekusi Koding Terkendali (Phase 4)

Setelah `TECH_SPEC.md` dan `PHASE_PLAN.md` disetujui, gunakan prompt library atomik:

```text
User: "Generate feature prompts untuk Module Orders."
Agent: Menghasilkan prompt per-fitur di docs/development/FEATURE_PROMPTS.md.

User: "Implementasikan Feature 1: Create Order menggunakan prompt dari library."
Agent: Memeriksa project conventions, lalu mengimplementasikan work item sesuai urutan dan batasan pada Tech Spec, Phase Plan, kontrak, dan prompt fitur terkait.
```

### 6. Validasi & Commit

Periksa checklist Definition of Done dan jalankan atomic commit:

```text
User: "Periksa kepatuhan DoD untuk fitur Create Order."
Agent: Menjalankan checklist aod-dod.

User: "Jalankan smart-git-commit."
Agent: Membagi perubahan menjadi atomic Conventional Commits.
```

---

## 📂 Struktur Output Dokumen

Semua artefak yang dihasilkan selama siklus AOD tersimpan rapi dalam folder `docs/`:

```text
docs/
├── business/
│   ├── BRD.md
│   ├── BUSINESS_FLOW.md
│   ├── PRD.md
│   ├── FLOWCHART.md
│   ├── RBAC.md
│   ├── DATA_DICTIONARY.md
│   └── SCHEMA.dbml
├── system-design/
│   ├── STATE_MACHINE.md
│   ├── API_CONTRACT.md
│   ├── UI_FLOW.md
│   ├── WEBSITE_CONCEPT.md
│   ├── DESIGN_SYSTEM.md
│   └── UI_STYLE.md
├── ui-architecture/
│   ├── COMPONENT_MAP.md
│   ├── UI_SLICING.md
│   └── DESIGN_TOKENS.md
├── development/
│   ├── TECH_SPEC.md
│   ├── PHASE_PLAN.md
│   ├── FEATURE_PROMPTS.md
│   └── DOD.md
├── testing/
│   └── UAT_SHEET.md
├── feedback/
│   ├── CR-001-payment-update.md
│   └── FINAL_REPORT_CR-001.md
├── proposal/
│   └── PROPOSAL.md
└── samples/
    ├── STUDY_CASE_DOCUMENT.md
    ├── FEEDBACK_TEMPLATE.md
    ├── UAT_SHEET_TEMPLATE.md
    ├── PROGRESS_REPORT_TEMPLATE.md
    └── FINAL_REPORT_TEMPLATE.md
```

---

## 🧩 Skill Ekosistem Pelengkap

Framework ini terintegrasi langsung dengan skill industri terverifikasi dari ekosistem agen:

- **`domain-modeling`** _(Matt Pocock)_: Menajamkan model domain, bounded context, dan relasi data.
- **`tailwind-design-system`** _(Wshobson)_: Pola implementasi sistem desain dan layout berbasis Tailwind v4/v3.
- **`tdd`** _(Matt Pocock)_: Alur implementasi kode _Test-Driven Development_ (Red-Green-Refactor).
- **`code-review`** _(Matt Pocock)_: Audit kualitas kode multi-axis sebelum merge.
- **`playwright-best-practices`** _(Currents.dev)_: Penulisan automated E2E tests berbasis skenario UAT.
- **`git-flow-branch-creator`** _(GitHub Awesome Copilot)_: Manajemen pembuatan branch git flow standar (`feature/*`, `release/*`, `hotfix/*`).
- **`git-workflow-and-versioning`** _(Addy Osmani)_: Best practices pengelolaan alur git, branching, dan semantic tagging.
- **`smart-git-commit`**: Pemilah commit git atomik berbasis Conventional Commits.
- **`antislop`**: Filter pencegah copy dan komponen UI bergaya AI generik.

---

## 👤 Author & Maintainer

Dikembangkan dan diarsiteki oleh:

**Oka R. Abdillah**

- **GitHub:** [@or-abdillh](https://github.com/or-abdillh)
- **Email:** [hans.abdillh05@gmail.com](mailto:hans.abdillh05@gmail.com)
- **Repository:** [AI-Orchestrated-Development-AOD](https://github.com/or-abdillh/AI-Orchestrated-Development-AOD)

---

## 📄 Lisensi

Didistribusikan di bawah lisensi MIT. Silakan gunakan, modifikasi, dan adaptasi untuk kebutuhan proyek perangkat lunak Anda.

## Pemeriksaan skill pack

Runtime helper dan installer: Bash dan Python 3 standard library. Instalasi
remote juga memerlukan tar serta curl atau wget. Installer memeriksa dependency,
mengganti hanya file paket dalam manifest dan blok AOD; file proyek, checkpoint,
dokumen produk, isi di luar marker dan aturan arsitektur proyek dipertahankan.
Marker rusak menyebabkan error, bukan pembaruan diam-diam.

Jalankan `python3 -m unittest discover -s tests -v`,
`python3 scripts/sync_workflow.py --check`, dan `bash -n install.sh`.
Pengujian fixture/state tidak membuktikan perilaku seluruh coding agent.

## Wizard instalasi terminal

Installer selalu menampilkan logo AOD. Saat terminal tersedia, wizard memberi
pilihan **pasang/perbarui**, **ubah direktori target**, **lihat isi paket**, dan
**batal**. Jawaban kosong pada menu tidak memulai instalasi. Progres menampilkan
jumlah file yang diperiksa dan ringkasan file baru, diperbarui, atau sudah sesuai.

```bash
# Wizard otomatis jika dijalankan dari terminal
bash install.sh /path/to/project

# Wajibkan wizard, termasuk saat stdout dialihkan
bash install.sh --interactive /path/to/project

# Tanpa prompt untuk CI atau otomatisasi
bash install.sh --yes /path/to/project

# Tanpa warna (juga mendukung environment NO_COLOR)
bash install.sh --no-color /path/to/project
```

Pemanggilan melalui pipe dapat memakai terminal pengendali untuk input wizard;
input tidak diambil dari stream skrip. Tanpa terminal, installer memakai mode
non-interaktif. `--interactive` gagal dengan pesan jelas bila terminal tidak
tersedia. Gunakan `--help` untuk melihat opsi.
