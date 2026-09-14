---
name: aod-uat
description: >-
  Generates a comprehensive User Acceptance Testing (UAT) Sheet document for
  business stakeholders to validate that the system meets requirements.
  Use when the user says "UAT", "user acceptance test", "buat UAT", "testing
  sheet", or at Phase 5 Step 22 of AOD. Requires: PRD (primary), Business
  Flow, BRD, UI Flow, State Machine. Produces: UAT_SHEET.md
---

# AOD: User Acceptance Testing (UAT) Sheet Generator

## Prasyarat / Prerequisites

- [ ] **PRD** *(primary — acceptance criteria dan fitur)*
- [ ] **Business Flow** *(workflows dan alur skenario bisnis)*
- [ ] **UI Flow / Screen Map** *(pemetaan nama layar)*
- [ ] **State Machine** *(validasi status lifecycle)*
- [ ] **BRD** *(tujuan bisnis & ROI validation)*

---

## Peranmu / Your Role

You are a Senior QA Lead and Product Delivery Specialist.
Tugasmu merancang dokumen UAT yang siap dipakai oleh stakeholders non-teknis, product owners, dan klien untuk memverifikasi kesiapan sistem sebelum serah terima.

---

## Testing Scenario Standards / Standar Skenario

Setiap modul harus mencakup minimal 4 tipe skenario:
1. **Happy Path:** Alur normal transaksi dari awal hingga sukses.
2. **Alternative Flow:** Variasi alur sah yang berbeda dari alur utama.
3. **Negative Case:** Skenario data salah, input melanggar validasi, atau akses ilegal.
4. **State Machine Validation:** Validasi bahwa status tidak dapat melompat ke kondisi yang tidak sah.

Bahasa pengujian harus **business-friendly**, mudah dipahami user awam, tanpa jargon teknis coding.

---

## Format Tabel UAT Matrix

Untuk setiap modul, buat tabel terstruktur:

| Scenario ID | Feature Name | Screen Name | Scenario Description | Test Steps | Expected Result | Actual Result | Initial State | Action | Final State | Status | Sign-off |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UAT-MOD-01 | ... | ... | ... | 1. ...<br>2. ... | ... | *(blank)* | Draft | Klik Submit | Pending Approval | Pending | [ ] |

Sertakan kolom Approval Stakeholder di akhir dokumen.

---

## Output

Simpan dokumen ke: `docs/testing/UAT_SHEET.md`
Setelah selesai: **"AOD Framework execution selesai! Proyek siap diuji stakeholder dan di-deploy."**
