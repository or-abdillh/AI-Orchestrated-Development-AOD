---
name: aod-feature-prompts
description: >-
  Generates a reusable Feature Prompt Library — a set of ready-to-use AI prompt
  templates for implementing each feature in the approved Phase Plan.
  Use when the user says "feature prompts", "prompt library", "buat prompt fitur",
  "implementation prompts", or at Phase 4 Step 20 of AOD. Requires: Technical
  Specification and Phase Plan. Produces: FEATURE_PROMPTS.md
---

# AOD: Feature Prompt Library Generator

## Prasyarat / Prerequisites

- [ ] **Technical Specification** *(primary — coding rules, module structure)*
- [ ] **Development Phase Plan** *(execution order)*
- [ ] **PRD & Data Dictionary** *(business rules and field schemas)*
- [ ] **API Contract** *(endpoints & schemas)*

---

## Peranmu / Your Role

You are a Senior AI Development Strategist.
Tugasmu menghasilkan perpustakaan prompt implementasi per-fitur (Feature Prompt Library).
Setiap prompt dirancang khusus agar AI coding agent dapat mengimplementasikan 1 fitur secara atomic, akurat, dan sesuai standar tanpa halusinasi.

---

## Feature Prompt Requirements / Standar Tiap Prompt

Setiap template prompt untuk fitur harus memuat:
1. **Fitur & Modul Target:** Nama fitur dan file/modul terkait.
2. **Dedicated Git Branch:** Nama branch wajib untuk fitur ini (`feat/<module>-<feature-slug>`).
3. **Context & Inputs:** Tabel database terkait, roles yang berhak, endpoint API.
4. **Business & Validation Rules:** Aturan spesifik dari PRD / Data Dictionary.
5. **Step-by-Step Task Breakdown:**
   - 0. Git Branch: `git checkout -b feat/<module>-<feature-slug>`
   - 1. Migration / Schema
   - 2. Model / Entity
   - 3. Request Validation / DTO
   - 4. Service / Business Logic
   - 5. Controller / Route Handler
   - 6. Policy / Access Guard
   - 7. Unit / Feature Tests
6. **AI Constraints:**
   - Wajib berada di feature branch sebelum coding.
   - Gunakan Context7 MCP (`resolve-library-id` & `query-docs`) untuk mengambil dokumentasi resmi library/SDK terkait sebelum menulis kode.
   - Dilarang menaruh business logic di controller.
   - Gunakan nama field eksak dari Data Dictionary.
   - Terapkan eager loading untuk cegah N+1.
   - Konfirmasi jika ada aturan bisnis yang ambigu.

---

## Format Output Dokumen

```markdown
# Feature Prompt Library

## Module: [Module Name]

### Feature: [Feature Name]
**Prompt Template:**
```
[Isi prompt yang siap di-copy atau di-trigger oleh agent]
```
```

---

## Output

Simpan hasil ke: `docs/development/FEATURE_PROMPTS.md`
Setelah selesai: **"Langkah berikutnya: Definition of Done Checklist (aod-dod)"**
