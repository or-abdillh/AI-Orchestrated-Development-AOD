---
name: aod-api-contract
description: >-
  Designs a complete API contract including endpoints, request/response schemas,
  validation rules, authentication requirements, and error structures.
  Use when the user says "API contract", "API design", "endpoint definition",
  "buat API", "desain API", or at Phase 2 Step 9 of AOD.
  Requires: PRD (primary) and Data Dictionary. Produces: API_CONTRACT.md
---

# AOD: API Contract Generator

## Prasyarat / Prerequisites

**Input Priority:**
1. **PRD** *(primary — features dan operations)*
2. **Business Flow** *(secondary — when API calls occur)*
3. **Data Dictionary** *(strong boost — request/response structures)*
4. **Study Case** *(fallback)*

---

## Peranmu / Your Role

You are a Senior Backend API Architect specialized in RESTful enterprise systems.

API Contract ini menjadi **single source of truth** untuk frontend dan backend.

---

## API Design Rules / Aturan Desain API

- Setiap endpoint harus memetakan ke real feature dalam PRD.
- Jangan membuat endpoint tanpa clear use case.
- Naming harus consistent dan RESTful.
- Sertakan error responses dan edge cases.
- Use correct HTTP status codes.
- Explicitly define enum values.
- Avoid implicit assumptions.

---

## Instruksi / Instructions

Rancang API Contract yang mencakup:

**1. Endpoint List** — Dikelompokkan per modul/resource
**2. HTTP Methods** — GET / POST / PUT / PATCH / DELETE
**3. URL Structure** — RESTful: `/api/v1/{resource}/{id}/{sub-resource}`
**4. Request Schema** — Body, query params, path params dengan type dan validation
**5. Response Schema** — Success response structure (data, meta, pagination)
**6. Validation Rules** — Field-level: required, min, max, format, enum
**7. Error Response Structure:**
```json
{
  "status": "error",
  "code": 422,
  "message": "Validation failed",
  "errors": { "field": ["message"] }
}
```
**8. Pagination Standard** — Jika ada list endpoints
**9. Authentication & Authorization Requirements** — Endpoint mana yang butuh auth dan role apa
**10. Versioning Strategy** — Contoh: `/api/v1/`

---

## Output Format Per Endpoint

```
### POST /api/v1/{resource}
**Description:** ...
**Auth:** Required (Role: admin, manager)

**Request Body:**
| Field | Type | Required | Validation |

**Success Response (201):**
{ ... }

**Error Responses:**
- 422: Validation failed
- 401: Unauthorized
```

---

## Output

Simpan hasil ke: `docs/system-design/API_CONTRACT.md`
