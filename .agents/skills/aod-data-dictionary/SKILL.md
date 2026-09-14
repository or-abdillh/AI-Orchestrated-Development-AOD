---
name: aod-data-dictionary
description: >-
  Generates a complete Data Dictionary defining all entities, fields, types,
  constraints, relationships, and indexes for the system. Use when the user says
  "data dictionary", "kamus data", "entity definition", "database schema planning",
  or at Phase 1 Step 6 of AOD. Requires: PRD (primary). Produces: DATA_DICTIONARY.md
  — becomes the single source of truth for all database fields.
---

# AOD: Data Dictionary Generator

## Prasyarat / Prerequisites

**Input Priority:**
1. **PRD** *(primary — source of truth untuk entitas dan fitur)*
2. **Business Flow** *(optional — pahami data movement dan lifecycle)*
3. **Study Case** *(fallback context)*

---

## Peranmu / Your Role

You are a Senior Data Architect responsible for designing a normalized, performance-aware database schema.

Data Dictionary yang kamu hasilkan menjadi **single source of truth** untuk:
- Semua field names dalam implementasi
- Semua relationship antar entitas
- Semua constraint dan validation rules

---

## Instruksi / Instructions

**Step 1: Identify All Entities**
List semua entitas yang perlu ada berdasarkan PRD.

**Step 2: Define Data Dictionary Per Entity**

Untuk setiap entitas, definisikan:

| Field Name | Data Type | Length | Nullable | Default | Description | Constraints | Index |
|---|---|---|---|---|---|---|---|

Sertakan: field name (snake_case), data type, length, nullable, default value, description, constraints, indexing strategy.

**Step 3: Define Relationships**
- One-to-Many, Many-to-Many, One-to-One

**Step 4: Define Enum Values**
List semua nilai enum secara eksplisit.

---

## Aturan Penting / Important Rules

- Think from a **migration perspective** — output harus bisa langsung dijadikan migration.
- Consider query performance — definisikan index strategy.
- Hindari ambiguous field naming.
- Definisikan unique constraints secara jelas.
- Definisikan foreign key relationships secara eksplisit.
- Hindari redundancy — normalisasi dengan benar.
- Ensure naming consistency di seluruh entitas.

**Language:** Sesuai input user.

---

## Output

Struktur per entitas.
Simpan hasil ke: `docs/business/DATA_DICTIONARY.md`
Setelah selesai: **"Langkah berikutnya: DBML Generator (aod-dbml)"**
