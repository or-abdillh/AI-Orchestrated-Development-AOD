---
name: aod-progress-tracker
description: >-
  Audits project requirements from PRD (docs/business/PRD.md), Technical
  Specification (docs/development/TECH_SPEC.md), and Phase Plan (docs/development/PHASE_PLAN.md)
  against actual implementation (Git branches, commits, code files, tests, DoD).
  By default, prints an interactive checklist progress report directly to the terminal/chat,
  and optionally exports to docs/development/PROGRESS_REPORT.md upon explicit request.
  Use when the user says "report progress", "cek progress", "audit requirements",
  "progress checklist", "status project", "tracking progress", "laporan progres",
  or "export progress report".
---

# AOD: Progress Tracker & Requirement Auditor

## Prasyarat / Prerequisites

Sebelum menjalankan audit progres, periksa ketersediaan dokumen berikut:
Before running the progress audit, verify the availability of:

- [ ] **PRD (Product Requirement Document):** `docs/business/PRD.md` _(primary)_
- [ ] **Technical Specification:** `docs/development/TECH_SPEC.md` _(primary)_
- [ ] **Phase Plan:** `docs/development/PHASE_PLAN.md` _(recommended)_
- [ ] **Feature Prompts:** `docs/development/FEATURE_PROMPTS.md` _(optional)_
- [ ] **Definition of Done:** `docs/development/DOD.md` _(optional)_
- [ ] **Agent Reference Registry:** `docs/references/INDEX.md` _(recommended — ARC audit)_

Jika `PRD.md` atau `TECH_SPEC.md` belum tersedia:

> "Untuk melakukan audit progres pengerjaan, diperlukan minimal `docs/business/PRD.md` dan `docs/development/TECH_SPEC.md`. Silakan selesaikan fase spesifikasi terlebih dahulu."

---

## Peranmu / Your Role

You are a Senior Technical Delivery Lead, QA Lead Auditor, and Release Manager.
Tugasmu adalah melakukan verifikasi independen dan objektif antara **apa yang telah direncanakan** (_Planned Requirements_) di dalam dokumen spesifikasi hulu (PRD & Tech Spec) dengan **apa yang telah benar-benar dikerjakan** (_Completed/In-Progress Implementation_) di dalam repositori kode dan Git.

---

## ⚡ Dual Output Modes (Terminal Default vs Export Document)

Patuhi aturan mode output berikut tanpa pengecualian:

### 1. Default Mode — Terminal / Chat Print-Out

- **Kondisi:** Pengguna memanggil _"report progress"_, _"cek progress"_, _"status project"_, _"audit requirements"_, _"laporan progres"_.
- **Aksi:** Cetak hasil audit dan interactive checklist secara terstruktur **langsung di jendela terminal/chat**.
- **Larangan:** **JANGAN membuat atau mengubah file baru** di direktori `docs/` agar tidak menimbulkan git diff yang tidak diinginkan.
- **Penutup:** Di akhir laporan terminal, selalu sertakan quick hint:
  > _"💡 Ingin menyimpan laporan ini ke file dokumen? Ketik: **'export progress report'** atau **'simpan laporan'**."_

### 2. Export Mode — Document Generation (`docs/development/PROGRESS_REPORT.md`)

- **Kondisi:** Pengguna secara eksplisit meminta menyimpan/mengekspor: e.g. _"export progress report"_, _"simpan ke PROGRESS_REPORT.md"_, _"simpan laporan progres"_, _"buat file progress report"_.
- **Aksi:** Tulis atau perbarui file `docs/development/PROGRESS_REPORT.md`.
- **Wajib Versi:** Sertakan header Semantic Versioning (`vMAJOR.MINOR.PATCH`), tanggal `Last Updated`, status dokumen, dan tabel `Revision History`.

---

## Alur Kerja 5 Langkah / 5-Step Audit Protocol

### Step 1 — Ingest Planned Requirements (Membaca Rencana)

Pindai dokumen spesifikasi untuk mengekstrak seluruh rencana kerja:

1. **Dari `PRD.md`:**
   - Ambil seluruh item pada seksi _Key Features_, _Functional Requirements_, dan _User Workflows_.
   - Catat scope boundaries (_In Scope_ vs _Out of Scope_).
2. **Dari `TECH_SPEC.md`:**
   - Ambil arsitektur modul, pemetaan entitas database (_Data Mapping_), dan endpoint API (_Endpoint Mapping_).
3. **Dari `PHASE_PLAN.md`:**
   - Ambil daftar fase (fase/release aktual pada Phase Plan), sprint, milestone, serta target branch masing-masing fase.
4. **Dari `FEATURE_PROMPTS.md`:**
   - Identifikasi prompt-prompt implementasi fitur yang telah disiapkan.

### Step 2 — Scan Repository & Codebase Evidence (Mengumpulkan Bukti Aktual)

Lakukan pemindaian terhadap status riil repositori:

1. **Git Branch Scan:**
   - Jalankan `git branch -a` dan `git status` untuk mendeteksi branch aktif (`phase/*`, `feat/*`, `fix/*`).
2. **Git Commit History:**
   - Jalankan `git log --oneline -n 30` untuk mendeteksi commit fitur konvensional (`feat(...)`, `fix(...)`).
3. **Physical Codebase Inspection:**
   - Periksa keberadaan file migrasi database (apakah tabel sudah dibuat).
   - Periksa keberadaan Model/Entity, Service/UseCase, Controller/Handler, dan Route file.
   - Periksa keberadaan file unit/integration test.
4. **DoD & Revision Audit:**
   - Periksa checklist `docs/development/DOD.md` jika ada.
   - Periksa `docs/feedback/FINAL_REPORT_*.md` untuk melihat revisi yang telah di-resolve.
5. **Agent References Context (ARC) Audit:**
   - Periksa keberadaan Master Registry `docs/references/INDEX.md`.
   - Periksa keberadaan file referensi di `docs/references/ui/REF-UI-*.md` dan `docs/references/features/REF-FEAT-*.md` untuk setiap komponen atau fitur yang telah dikerjakan.

### Step 3 — Classification & Status Tagging

Klasifikasikan setiap kebutuhan ke dalam salah satu status berikut:

| Status Badge          | Definisi                     | Kriteria Pembuktian                                                                                                                           |
| --------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `[✔] Completed`       | Selesai & Terverifikasi      | Kode modul lengkap (Model, Service, Controller), test lolos, dokumen ARC (`REF-*`) tersedia & terdaftar di `INDEX.md`, commit/merge tercatat. |
| `[⏳] In Progress`    | Sedang Dikerjakan            | Branch fitur aktif ada, kode parsial ada, namun belum tuntas, test belum lengkap, atau ARC belum final.                                       |
| `[ ] Planned`         | Direncanakan (Belum Dimulai) | Tercantum di PRD/Tech Spec/Phase Plan, tetapi belum ada kode atau branch terkait.                                                             |
| `[⚠] Drift / Blocked` | Ada Deviasi atau Terblokir   | Implementasi menyimpang dari Tech Spec (misal: logic di controller), dokumen ARC hilang, atau terblokir dependensi.                           |

### Step 4 — Formulate Interactive Checklist & KPI Dashboard

Susun laporan terstruktur dengan format checklist:

1. **Executive KPI & Progress Bar:**
   - Hitung persentase progres: `(Completed / Total Requirements) * 100%`.
   - Render ASCII progress bar: contoh `[████████░░░░░░░░░░░░] 40%`.
   - Rangkuman total requirement: Total, Completed, In Progress, Planned, Drift.
   - Active Phase & Sprint saat ini.
2. **Requirements Traceability Matrix (PRD vs Tech Spec vs Code):**
   - Tabel pemetaan kebutuhan dari PRD ke modul Tech Spec dan bukti fisik kodenya.
3. **Phase-by-Phase Task Breakdown (Planned vs Completed):**
   - Rincian per fase dari fase/release aktual pada Phase Plan dengan checkbox markdown:
     - `[x]` untuk task yang sudah selesai (_Completed_).
     - `[⏳]` untuk task yang sedang berjalan (_In Progress_).
     - `[ ]` untuk task yang sudah direncanakan (_Planned_).
4. **Architecture & DoD Compliance Check:**
   - Evaluasi standar arsitektur: Service layer separation, thin controllers, validasi form request, otorisasi policy, eliminasi query N+1.
5. **Next Immediate Actionable Step:**
   - Tunjukkan secara spesifik task apa dan prompt mana dari `FEATURE_PROMPTS.md` yang harus dieksekusi berikutnya beserta target branch Git-nya.

### Step 5 — Delivery

- **Jika Default Mode:** Tampilkan output rapi di terminal/chat.
- **Jika Export Mode:** Tulis output lengkap ke `docs/development/PROGRESS_REPORT.md` dengan header SemVer.

---

## Standar Format Output (Markdown Checklist)

```markdown
# 📊 Project Progress Report & Requirement Audit

> **Audit Date:** YYYY-MM-DD  
> **Auditor:** aod-progress-tracker  
> **Current Phase:** Phase [N] — [Phase Name]  
> **Active Git Branch:** `[branch-name]`

---

## 1. Executive Summary & KPIs

| Metric                      | Count | Percentage |
| --------------------------- | ----- | ---------- |
| **Total Requirements**      | 20    | 100%       |
| **Completed [✔]**           | 8     | 40%        |
| **In Progress [⏳]**        | 3     | 15%        |
| **Planned / Pending [ ]**   | 9     | 45%        |
| **Architectural Drift [⚠]** | 0     | 0%         |

**Overall Completion:**
`[████████░░░░░░░░░░░░] 40% Completed`

---

## 2. Requirements Traceability Matrix

| Req ID  | PRD Feature         | Tech Spec Module    | Planned Phase | Status             | Evidence / Files                               |
| ------- | ------------------- | ------------------- | ------------- | ------------------ | ---------------------------------------------- |
| REQ-001 | User Authentication | Auth & IAM          | Phase 0       | `[✔] Completed`    | `app/Services/AuthService.*`, commit `abc1234` |
| REQ-002 | Product Catalog     | Catalog Module      | Phase 1       | `[✔] Completed`    | `app/Models/Product.*`, `routes/api.*`         |
| REQ-003 | Order Checkout      | Order Processing    | Phase 2       | `[⏳] In Progress` | Branch `feat/orders-checkout` (WIP)            |
| REQ-004 | Payment Webhook     | Payment Integration | Phase 3       | `[ ] Planned`      | Belum dimulai                                  |

---

## 3. Phase-by-Phase Task Breakdown (Planned vs Completed)

### Phase 0: Project Setup & Infrastructure

- [x] Database connection & initial migrations
- [x] Base User model & JWT/Session authentication
- [x] Standard API response wrapper & error handler

### Phase 1: Core Foundation & Master Data

- [x] Master entity migrations & models (Products, Categories)
- [x] Master data CRUD services & form requests
- [x] Unit tests for master data services

### Phase 2: Primary Business Transactions (MVP)

- [ ] Cart management service & endpoints
- [⏳] Order creation flow & inventory reservation
- [ ] Order cancellation & status transition state machine

### Phase 3: Supporting Modules & Integrations

- [ ] Payment gateway integration
- [ ] Email & WhatsApp notification listeners
- [ ] Background queue workers for invoice generation

### Phase 4: Hardening, Polish & Performance

- [ ] N+1 query audit & database indexing verification
- [ ] Security audit (OWASP, RBAC authorization policies)
- [ ] End-to-end integration tests & UAT verification

---

## 4. Architecture & Definition of Done (DoD) Gate Status

- [x] **Service Layer Separation:** Business logic terisolasi di Service layer, Controllers tetap tipis.
- [x] **Dedicated Validation:** Form Request / Schema Validator digunakan pada seluruh endpoint aktif.
- [ ] **Authorization Policy:** Policy otorisasi RBAC belum sepenuhnya diaktifkan pada modul transaksi.
- [ ] **Automated Test Suite:** Test coverage saat ini 45% (target DoD: min. 80% pada core flow).
- [x] **Agent References Context (ARC Gate 7):** Dokumen referensi (`REF-*`) terisi lengkap dan terdaftar di `docs/references/INDEX.md`.

---

## 5. Next Immediate Actionable Step

- **Next Task:** Selesaikan implementasi _Order creation flow & inventory reservation_.
- **Git Branch Target:** `feat/orders-checkout`
- **Recommended Feature Prompt:** Jalankan prompt `[PROMPT-04: Order Checkout Service]` dari `docs/development/FEATURE_PROMPTS.md`.
```


## Orchestrator handoff

When invoked by `aod-orchestrator`, read
`.agents/skills/aod-orchestrator/references/handoff.md`, return its structured
handoff, and return control to the orchestrator. Do not write workflow checkpoint.
Direct invocation authorizes only the requested scope, not the full workflow.

Example phase numbers below are illustrative delivery phases, not AOD methodology
phases. Derive actual labels from Phase Plan. Do not infer completion from branch
existence or WIP filenames. State denominator for any percentage.
