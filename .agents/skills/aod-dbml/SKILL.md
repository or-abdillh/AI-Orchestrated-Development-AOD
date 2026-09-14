---
name: aod-dbml
description: >-
  Converts a Data Dictionary into a clean, valid DBML schema ready for ERD
  visualization tools. Use when the user says "DBML", "generate schema",
  "ERD schema", "buat DBML", or at Phase 1 Step 7 of AOD.
  Requires: Data Dictionary. Produces: SCHEMA.dbml
---

# AOD: DBML Schema Generator

## Prasyarat / Prerequisites

- [ ] **Data Dictionary** *(required — SCHEMA.md atau paste langsung)*

Jangan buat DBML jika Data Dictionary belum finalized.
Setiap field dalam DBML harus berasal dari Data Dictionary.

---

## Peranmu / Your Role

You are a Senior Data Architect and Database Designer.

---

## Analisis Sebelum Generate / Pre-Generation Analysis

Identifikasi:
1. Semua entitas → Tables
2. Fields per entitas
3. Primary keys, Foreign keys, Unique constraints
4. Default values, Nullable fields, Index strategies
5. Enumerations, Relationships

Do NOT invent entities or fields not in the Data Dictionary.

---

## DBML Structure Rules

Tables:
```dbml
Table users {
  id uuid [pk]
  name varchar(255) [not null]
  email varchar(255) [unique, not null]
  created_at timestamp [default: `now()`]
}
```

Enums:
```dbml
Enum order_status {
  pending
  processing
  completed
  cancelled
}
```

Indexes:
```dbml
Indexes {
  (email) [unique]
}
```

References:
```dbml
Ref: orders.user_id > users.id
```

---

## Naming Conventions

- Tables: `snake_case` plural
- Columns: `snake_case`
- Foreign keys: `{entity}_id`
- Enum types: `{entity}_{field}`

---

## Output

Return ONLY the DBML schema in a dbml code block.
Simpan hasil ke: `docs/business/SCHEMA.dbml`

**Business Layer selesai.** → Phase 2: System Design
