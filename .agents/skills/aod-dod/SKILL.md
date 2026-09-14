---
name: aod-dod
description: >-
  Generates a Definition of Done (DoD) checklist for validating every feature
  across functional correctness, code quality, security, testing, and UI
  compliance. Use when the user says "definition of done", "DoD", "checklist
  selesai", "feature complete checklist", or at Phase 4 Step 21 of AOD.
  Requires: Technical Specification and Phase Plan. Produces: DOD.md
---

# AOD: Definition of Done (DoD) Checklist Generator

## Prasyarat / Prerequisites

- [ ] **Technical Specification** *(system correctness criteria)*
- [ ] **Feature Prompt Library & Phase Plan** *(scope and sequence)*
- [ ] **PRD & Business Flow** *(functional expectations)*
- [ ] **State Machine & API Contract** *(data & state integrity)*

---

## Peranmu / Your Role

You are a Senior Software Quality Auditor.
Tugasmu membuat checklist Definition of Done yang tegas, terukur, dan praktis untuk memastikan tidak ada kode yang masuk ke fase rilis tanpa memenuhi standar mutu.

---

## DoD Categories / Kategori Checklist

Checklist harus mencakup 6 pilar:

### 1. Functional & Business Logic
- [ ] Alur kerja sesuai dengan use case PRD dan Business Flow.
- [ ] Transisi status mematuhi State Machine (termasuk invalid transition prevention).
- [ ] Edge cases dan failure scenarios tertangani dengan ramah user.

### 2. Code Architecture & Cleanliness
- [ ] Layering konsisten sesuai Tech Spec (e.g. Service Layer untuk business logic).
- [ ] Tidak ada logic acak di controller/route handlers.
- [ ] Penamaan variabel, fungsi, dan entity selaras dengan Data Dictionary.

### 3. Data Integrity & Validation
- [ ] Semua input divalidasi ketat di request layer (tipe, range, format, enum).
- [ ] Database transaction digunakan pada operasi multi-table write.
- [ ] Soft deletes / cascade rules diuji jika ada.

### 4. Security & Access Control
- [ ] Authorization policy / role checks aktif di setiap endpoint/action.
- [ ] Tidak ada data sensitif (password hash, internal token) bocor di response.
- [ ] Bebas dari kerentanan umum (SQL injection, XSS, CSRF, IDOR).

### 5. Performance & Resource Hygiene
- [ ] Bebas dari issue N+1 query (eager loading digunakan).
- [ ] Kolom pencarian/filter memiliki index yang memadai.
- [ ] Response payload terukur dan terpaginasi untuk dataset besar.

### 6. Automated Testing
- [ ] Unit / Feature tests tersedia untuk happy path dan negative path.
- [ ] Semua test suite berjalan hijau (passing) sebelum commit.

---

## Output

Simpan dokumen ke: `docs/development/DOD.md`
Setelah selesai: **"Langkah berikutnya: User Acceptance Testing (aod-uat)"**
