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

- [ ] **PRD (Product Requirement Document):** `docs/business/PRD.md` *(primary)*
- [ ] **Technical Specification:** `docs/development/TECH_SPEC.md` *(primary)*
- [ ] **Phase Plan:** `docs/development/PHASE_PLAN.md` *(recommended)*
- [ ] **Feature Prompts:** `docs/development/FEATURE_PROMPTS.md` *(optional)*
- [ ] **Definition of Done:** `docs/development/DOD.md` *(optional)*

Jika `PRD.md` atau `TECH_SPEC.md` belum tersedia:
> "Untuk melakukan audit progres pengerjaan, diperlukan minimal `docs/business/PRD.md` dan `docs/development/TECH_SPEC.md`. Silakan selesaikan fase spesifikasi terlebih dahulu."

---

## Peranmu / Your Role

You are a Senior Technical Delivery Lead, QA Lead Auditor, and Release Manager.
Tugasmu adalah melakukan verifikasi independen dan objektif antara **apa yang telah direncanakan** (*Planned Requirements*) di dalam dokumen spesifikasi hulu (PRD & Tech Spec) dengan **apa yang telah benar-benar dikerjakan** (*Completed/In-Progress Implementation*) di dalam repositori kode dan Git.

---

## ⚡ Dual Output Modes (Terminal Default vs Export Document)

Patuhi aturan mode output berikut tanpa pengecualian:

### 1. Default Mode — Terminal / Chat Print-Out
- **Kondisi:** Pengguna memanggil *"report progress"*, *"cek progress"*, *"status project"*, *"audit requirements"*, *"laporan progres"*.
- **Aksi:** Cetak hasil audit dan interactive checklist secara terstruktur **langsung di jendela terminal/chat**.
- **Larangan:** **JANGAN membuat atau mengubah file baru** di direktori `docs/` agar tidak menimbulkan git diff yang tidak diinginkan.
- **Penutup:** Di akhir laporan terminal, selalu sertakan quick hint:
  > *"💡 Ingin menyimpan laporan ini ke file dokumen? Ketik: **'export progress report'** atau **'simpan laporan'**."*

### 2. Export Mode — Document Generation (`docs/development/PROGRESS_REPORT.md`)
- **Kondisi:** Pengguna secara eksplisit meminta menyimpan/mengekspor: e.g. *"export progress report"*, *"simpan ke PROGRESS_REPORT.md"*, *"simpan laporan progres"*, *"buat file progress report"*.
- **Aksi:** Tulis atau perbarui file `docs/development/PROGRESS_REPORT.md`.
- **Wajib Versi:** Sertakan header Semantic Versioning (`vMAJOR.MINOR.PATCH`), tanggal `Last Updated`, status dokumen, dan tabel `Revision History`.

---

## Alur Kerja 5 Langkah / 5-Step Audit Protocol

### Step 1 — Ingest Planned Requirements (Membaca Rencana)
Pindai dokumen spesifikasi untuk mengekstrak seluruh rencana kerja:
1. **Dari `PRD.md`:**
   - Ambil seluruh item pada seksi *Key Features*, *Functional Requirements*, dan *User Workflows*.
   - Catat scope boundaries (*In Scope* vs *Out of Scope*).
2. **Dari `TECH_SPEC.md`:**
   - Ambil arsitektur modul, pemetaan entitas database (*Data Mapping*), dan endpoint API (*Endpoint Mapping*).
3. **Dari `PHASE_PLAN.md`:**
   - Ambil daftar fase (Phase 0 s/d Phase 4), sprint, milestone, serta target branch masing-masing fase.
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

### Step 3 — Classification & Status Tagging
Klasifikasikan setiap kebutuhan ke dalam salah satu status berikut:

| Status Badge | Definisi | Kriteria Pembuktian |
|---|---|---|
| `[✔] Completed` | Selesai & Terverifikasi | Kode modul lengkap (Model, Service, Controller), test ada/lolos, commit/merge tercatat. |
| `[⏳] In Progress` | Sedang Dikerjakan | Branch fitur aktif ada, kode parsial ada, namun belum tuntas atau test belum lengkap. |
| `[ ] Planned` | Direncanakan (Belum Dimulai) | Tercantum di PRD/Tech Spec/Phase Plan, tetapi belum ada kode atau branch terkait. |
| `[⚠] Drift / Blocked` | Ada Deviasi atau Terblokir | Implementasi menyimpang dari Tech Spec (misal: logic di controller) atau terblokir dependensi. |

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
   - Rincian per fase dari Phase 0 hingga Phase 4 dengan checkbox markdown:
     - `[x]` untuk task yang sudah selesai (*Completed*).
     - `[⏳]` untuk task yang sedang berjalan (*In Progress*).
     - `[ ]` untuk task yang sudah direncanakan (*Planned*).
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

| Metric | Count | Percentage |
|---|---|---|
| **Total Requirements** | 20 | 100% |
| **Completed [✔]** | 8 | 40% |
| **In Progress [⏳]** | 3 | 15% |
| **Planned / Pending [ ]** | 9 | 45% |
| **Architectural Drift [⚠]** | 0 | 0% |

**Overall Completion:**
`[████████░░░░░░░░░░░░] 40% Completed`

---

## 2. Requirements Traceability Matrix

| Req ID | PRD Feature | Tech Spec Module | Planned Phase | Status | Evidence / Files |
|---|---|---|---|---|---|
| REQ-001 | User Authentication | Auth & IAM | Phase 0 | `[✔] Completed` | `app/Services/AuthService.*`, commit `abc1234` |
| REQ-002 | Product Catalog | Catalog Module | Phase 1 | `[✔] Completed` | `app/Models/Product.*`, `routes/api.*` |
| REQ-003 | Order Checkout | Order Processing | Phase 2 | `[⏳] In Progress` | Branch `feat/orders-checkout` (WIP) |
| REQ-004 | Payment Webhook | Payment Integration | Phase 3 | `[ ] Planned` | Belum dimulai |

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

---

## 5. Next Immediate Actionable Step

- **Next Task:** Selesaikan implementasi *Order creation flow & inventory reservation*.
- **Git Branch Target:** `feat/orders-checkout`
- **Recommended Feature Prompt:** Jalankan prompt `[PROMPT-04: Order Checkout Service]` dari `docs/development/FEATURE_PROMPTS.md`.
```
