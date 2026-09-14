# AOD Coding Standards — Development Phase

> Active during Development Phase (aod-tech-spec, aod-phase-plan, aod-feature-prompts, aod-dod).
> These rules govern how AI generates implementation code.
> Adapt to the tech stack confirmed in the Technical Specification.

---

## Core Architecture Rules / Aturan Arsitektur Inti

- Follow the architecture pattern defined in Technical Specification. Do not deviate.
- Business logic belongs in the Service/Use Case layer, NOT in Controllers/Routes.
- Controllers are thin: receive request, delegate to service, return response.
- Models/Entities contain relationships and domain rules only.
- Validation must use dedicated Request/FormRequest/Schema classes.
- Authorization must use dedicated Policy/Guard/Permission classes.

## Implementation Discipline / Disiplin Implementasi

- Only implement features defined in the Feature Prompt. Do not add unrequested features.
- Do not rename fields. Use exact field names from the Data Dictionary.
- Do not create endpoints not defined in the API Contract.
- Do not assume undefined schema. Ask clarification if a field is ambiguous.
- If a business rule is unclear, stop and ask — do not guess.

## Code Quality Rules / Aturan Kualitas Kode

- N+1 queries are a defect. Use eager loading where relationships are accessed.
- Each feature must include appropriate input validation.
- Each data-modifying feature must include authorization checks.
- Error responses must follow the format defined in the API Contract.
- Do not place raw queries in controllers unless absolutely necessary.

## Scope Control / Kendali Scope

- Do not over-engineer. Match complexity to the project's stated scope (SME/freelance).
- Do not introduce design patterns not specified in the Technical Specification.
- Do not change database schema without user approval.
- Feature is DONE only when it passes the Definition of Done checklist (aod-dod).

## Framework Agnosticism

- These rules apply regardless of tech stack.
- Specific framework conventions are defined in the Technical Specification.
- When in doubt about framework-specific patterns, refer to the Tech Spec first.

---

## Git Branching Strategy / Strategi Git Branching (MANDATORY)

Setiap implementasi kode pada Phase Development **WAJIB** berada dalam git branch terisolasi:

1. **Dilarang Keras Langsung Commit ke `main`/`master`:**
   - Seluruh pekerjaan fitur baru harus dikerjakan di branch terpisah.
2. **Konvensi Penamaan Branch:**
   - **Phase Branch:** `phase/<phase-num>-<phase-slug>` (contoh: `phase/01-core-foundation`, `phase/02-order-management`)
   - **Feature Branch:** `feat/<module>-<feature-slug>` (contoh: `feat/orders-create-order`, `feat/auth-jwt-login`)
   - **Fix / Refactor Branch:** `fix/<module>-<issue-slug>` atau `refactor/<module>-<target-slug>`
3. **Alur Eksekusi Branching Per-Fitur:**
   ```bash
   # 1. Pastikan basis branch sinkron (develop atau phase branch aktif)
   git checkout develop || git checkout main
   git pull

   # 2. Buat branch baru untuk fitur yang akan dikerjakan
   git checkout -b feat/<module>-<feature-name>

   # 3. AI mengimplementasikan kode secara atomik (Task 1-8 pada Feature Prompt)
   # 4. Validasi kepatuhan Definition of Done (aod-dod)
   # 5. Commit atomik menggunakan Conventional Commits (smart-git-commit)
   # 6. Merge kembali ke phase branch setelah verifikasi lolos
   ```
4. **Skill Pendukung Git:**
   - Gunakan `git-flow-branch-creator` untuk memvalidasi alur Git Flow standar.
   - Gunakan `git-workflow-and-versioning` untuk panduan branching dan release tagging.
   - Gunakan `smart-git-commit` untuk eksekusi commit atomik.

