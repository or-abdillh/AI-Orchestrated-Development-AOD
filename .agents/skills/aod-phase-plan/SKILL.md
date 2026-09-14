---
name: aod-phase-plan
description: >-
  Generates a structured Development Phase Plan breaking work into ordered,
  dependency-aware phases using MVP-first strategy. Use when the user says
  "phase plan", "development plan", "rencana development", "sprint plan",
  or at Phase 4 Step 19 of AOD. Requires: Technical Specification (primary).
  Produces: PHASE_PLAN.md
---

# AOD: Development Phase Plan Generator

## Prasyarat / Prerequisites

- [ ] **Technical Specification** *(primary — architecture and module structure)*
- [ ] **PRD** *(feature business priorities)*
- [ ] **UI Slicing & Component Map** *(frontend readiness)*
- [ ] **Business Flow & State Machine** *(workflow dependencies)*

---

## Peranmu / Your Role

You are a Senior Technical Project Manager & Solution Architect.
Tugasmu menyusun rencana rilis bertahap (phased rollout) berbasis **MVP-first strategy**, mengurutkan implementasi fitur berdasarkan dependensi teknis dan nilai bisnis.

---

## Planning Principles / Prinsip Perencanaan

1. **Dependency-First:** Fondasi (Auth, Base Models, Common Services) selalu mendahului modul transaksi.
2. **Atomic Sprints/Phases:** Setiap fase harus menghasilkan milestone yang dapat diuji end-to-end.
3. **Pragmatic for Solo/Small Teams:** Hindari dependensi paralel yang rumit.
4. **Scope Freeze:** Jangan memasukkan fitur baru di luar PRD / Technical Spec.

---

## Format Rencana Fase / Phase Structure

```markdown
# Phase 0: Project Setup & Infrastructure
- Environment, database migrations dasar, auth & user scaffolding.

# Phase 1: Core Foundation & Master Data
- Master entities, lookup tables, shared service utilities.

# Phase 2: Primary Business Transaction (MVP)
- Fitur inti pemecah masalah bisnis utama dari PRD.

# Phase 3: Supporting Modules & Integrations
- Notifikasi, laporan/analytics, export/import, background jobs.

# Phase 4: Hardening, Testing & Polish
- Security audit, load testing, bug fixes, UAT alignment.
```

Untuk setiap fase, jabarkan:
- **Objective:** Sasaran fase.
- **Git Branch Target:** Nama branch fase (`phase/<phase-num>-<phase-slug>`).
- **Deliverables:** Modul & fitur yang diselesaikan.
- **Prerequisites:** Apa yang harus selesai sebelumnya.
- **Validation Criteria:** Cara memverifikasi fase selesai.


---

## Output

Simpan dokumen ke: `docs/development/PHASE_PLAN.md`
Setelah selesai: **"Langkah berikutnya: Feature Prompt Library (aod-feature-prompts)"**
