---
name: aod-ui-slicing
description: >-
  Generates a complete UI Slicing Document — building the full frontend UI
  structure with layouts, components, mock data, UI states, and folder structure
  before backend integration. Use when the user says "UI slicing", "buat UI",
  "frontend structure", "slicing document", or at Phase 3 Step 15 of AOD.
  Requires: UI Component Map (primary). Produces: UI_SLICING.md
---

# AOD: UI Slicing Document Generator

## Prasyarat / Prerequisites

- [ ] **UI Component Map** *(primary — single source of truth untuk component structure)*
- [ ] **Design System & UI Style Document** *(styling, tokens, theme)*
- [ ] **API Contract** *(untuk mock data generation)*
- [ ] **State Machine** *(untuk simulasi status badge/UI)*

UI Component Map adalah referensi mutlak hierarki komponen. Jangan improvisasi struktur halaman di luar dokumen ini.

---

## Peranmu / Your Role

You are a Senior Frontend Architect and UI Engineer.
Tugasmu merancang dokumen UI Slicing komprehensif yang menyiapkan arsitektur frontend sebelum integrasi backend, mendukung framework pilihan user (React/Next.js, Vue/Nuxt, Svelte, dsb.).

---

## Critical Rules / Aturan Utama

1. **No Real Backend Calls Yet:** Gunakan mock data realistis berdasarkan schema API Contract.
2. **State Simulation:** Visualisasikan setiap state dari State Machine (loading, empty, error, success, status tags).
3. **Design System Adherence:** Wajib mematuhi design tokens dari UI Style Document.
4. **Clean Folder Architecture:** Struktur folder harus modular, scalable, dan framework-appropriate.

---

## Struktur Dokumen Output / Output Structure

**1. Architectural Layouts**
Definisikan layout induk (AppLayout, AuthLayout, DashboardLayout, PublicLayout).

**2. Component Inventory & Classification**
Klasifikasikan komponen:
- UI Elements (Atoms): Button, Input, Badge, Spinner
- Patterns (Molecules/Organisms): DataTable, FilterBar, NavHeader
- Views/Pages (Templates)

**3. State & Visual Mapping**
Petakan setiap status dari State Machine ke representasi visual UI:
- e.g. `pending` → amber badge, `active` → emerald badge, `rejected` → rose badge.

**4. Realistic Mock Data Schema**
Definisikan mock datasets yang mencerminkan API Contract untuk keperluan preview/slicing.

**5. Page UI Skeletons & Wireframes**
Struktur kode kerangka (skeleton) per halaman utama.

**6. Frontend Folder Structure**
Rekomendasi struktur direktori bersih:
```text
src/
├── assets/
├── components/
│   ├── ui/
│   └── shared/
├── layouts/
├── pages/ or views/
├── mocks/
└── types/
```

**7. Integration Notes**
Panduan transisi saat backend API siap dihubungkan.

---

## Output

Simpan dokumen ke: `docs/ui-architecture/UI_SLICING.md`
Setelah selesai: **"Langkah berikutnya: CSS/Tailwind Config (aod-tailwind-config) dan Per-Page Slicing (aod-page-slicer)"**
