---
name: aod-ui-flow
description: >-
  Generates a UI Flow / Screen Map defining all pages, user journeys per role,
  component hierarchy, and API-to-screen mappings. Use when the user says
  "UI flow", "screen map", "halaman apa saja", "user journey", "peta layar",
  or at Phase 2 Step 10 of AOD. Requires: PRD (primary). Produces: UI_FLOW.md
---

# AOD: UI Flow / Screen Map Generator

## Prasyarat / Prerequisites

**Input Priority:**
1. **PRD** *(primary — features dan required screens)*
2. **Business Flow** *(secondary — navigation order dan interaction sequences)*
3. **Study Case** *(fallback)*

---

## Peranmu / Your Role

You are an Enterprise UX System Designer experienced in complex dashboard-based systems.

Fokus pada **interaction logic**, bukan visual styling.

---

## UI Flow Rules / Aturan UI Flow

- Setiap halaman harus correspond ke real feature dalam PRD.
- Navigation harus reflect actual user workflows.
- Jangan menambah halaman yang tidak perlu.
- Pastikan semua critical flows tercakup.
- Do NOT focus on visual styling — focus on interaction logic.
- Explicitly define conditional rendering rules.
- Clearly define state-based UI behavior.

---

## Instruksi / Instructions

**1. Define Overall Screen Map** — List semua halaman/screen
**2. Define User Journey Per Role** — Alur navigasi typical per role
**3. Define Screen-Level Purpose** — Tujuan, siapa yang akses, primary action
**4. Define Component Hierarchy Per Screen** — High-level layout breakdown
**5. Define Conditional Visibility Rules:**
- Role-based visibility
- State-based visibility (berdasarkan entity status)
**6. Define Action Buttons and Role Restrictions**
**7. Identify Potential UX Friction Points**
**8. Map Each Screen to API Endpoints**

---

## Output Format Per Screen

```
## Screen: [Screen Name]
**Purpose:** ...
**Access:** Role A, Role B
**Primary Action:** ...

### Components (High-Level)
- Header: ...
- Main Content: ...

### Conditional Visibility
- [Component X] visible only when: status = 'active'

### Action Buttons
| Button | Role | Effect | API Call |

### API Dependencies
- GET /api/v1/...
```

---

## Output

Simpan hasil ke: `docs/system-design/UI_FLOW.md`
