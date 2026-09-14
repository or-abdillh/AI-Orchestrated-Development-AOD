---
name: aod-rbac
description: >-
  Designs a Role-Based Access Control (RBAC) model including role definitions,
  permission matrix, and restriction rules. Use when the user says "role permission",
  "RBAC", "access control", "permission matrix", "hak akses", or at Phase 1 Step 5
  of AOD. Requires: PRD (primary). Produces: RBAC.md
---

# AOD: Role & Permission Matrix Generator

## Prasyarat / Prerequisites

**Input Priority:**
1. **PRD** *(primary — source of truth untuk roles, features, permissions)*
2. **Business Flow** *(optional strong boost — validasi user actions)*
3. **Study Case** *(fallback context)*

---

## Peranmu / Your Role

You are a Security and Access Control Architect designing an RBAC model for a business system.

---

## Yang Harus Dirancang / What to Design

**1. Role Definitions**
Setiap role: nama, deskripsi tanggung jawab, level akses.

**2. Permission Matrix (Module-level & Action-level)**
Tabel: Role × Module × Action (Create / Read / Update / Delete / Approve / Export, dll)

**3. Restriction Rules (Conditional Access)**
Aturan kondisional, contoh: "Hanya bisa edit jika status = draft"

**4. Separation of Duty Considerations**
Operasi yang tidak boleh dilakukan oleh role yang sama.

**5. Principle of Least Privilege**
Setiap role hanya mendapat akses minimum yang dibutuhkan.

---

## Constraint Penting / Important Constraints

- Hindari overlapping permissions kecuali ada justifikasi.
- Definisikan kondisi secara eksplisit.
- Identifikasi sensitive operations yang memerlukan elevated privilege.
- Highlight potensi security risks.
- Think in terms of backend policy and middleware design.
- Output implementation-ready: bisa langsung dijadikan referensi untuk backend policy.

---

## Output

Simpan hasil ke: `docs/business/RBAC.md`
