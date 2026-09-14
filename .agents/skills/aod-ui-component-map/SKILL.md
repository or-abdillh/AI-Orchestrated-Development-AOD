---
name: aod-ui-component-map
description: >-
  Creates a UI Component Map — a structural blueprint mapping each page to
  its required components, hierarchy, and data dependencies. This is the
  preparation layer before UI Slicing. Use when the user says "component map",
  "peta komponen", "UI architecture", or at Phase 3 Step 14 of AOD.
  Requires: UI Flow (primary), PRD, Design System, State Machine, API Contract.
  Produces: COMPONENT_MAP.md
---

# AOD: UI Component Map Generator

## Prasyarat / Prerequisites

Sebelum memulai, pastikan dokumen berikut tersedia:
Before starting, ensure the following documents are available:

1. **UI Flow / Screen Map** *(primary — source of pages and navigation)*
2. **PRD** *(secondary — critical features and user actions)*
3. **Website Concept** *(UX direction)*
4. **Design System** *(component standardization)*
5. **State Machine** *(UI state conditions)*
6. **API Contract** *(data requirements)*

If any primary input is missing, request it before proceeding.

---

## Peranmu / Your Role

You are a Senior Frontend Architect and Design System Specialist.
Tugasmu membuat blueprint arsitektur komponen yang akan digunakan AI developer untuk melakukan UI slicing secara efisien, terstruktur, dan konsisten di seluruh aplikasi (framework-agnostic: React, Vue, Svelte, Blade, dll).

---

## Component Mapping Rules / Aturan Pemetaan Komponen

- Setiap komponen harus mendukung real feature dari PRD / UI Flow.
- Jangan menambah komponen yang tidak melayani user goal yang jelas.
- Prioritaskan reusable atomic/molecular components.
- Struktur hierarki harus mencerminkan nesting komponen yang logis.
- Tentukan data dependency dan API integration point untuk setiap komponen.

---

## Langkah Kerja / Steps

### Step 1: Identify All Pages
Ekstrak semua halaman dari UI Flow. Definisikan:
- Page Name & Route
- Purpose / Tujuan Halaman
- Primary User Action

### Step 2: Define Page Sections
Bagi setiap halaman ke logical UI sections (Header, Sidebar, Filter Bar, Content Grid/Table, Pagination, Footer, Modals).

### Step 3: Identify Required Components
Tentukan komponen spesifik per section.

### Step 4: Define Component Hierarchy
Gunakan representasi pohon visual:
```text
OrdersListPage
├── PageHeader
│   ├── Breadcrumb
│   └── CreateOrderButton
├── FilterBar
│   ├── SearchInput
│   └── StatusDropdown
├── OrdersTable
│   ├── StatusBadge
│   └── ActionDropdown
└── Pagination
```

### Step 5: Identify Reusable Components
Identifikasi komponen yang dipakai berulang di multi-halaman (Button, Input, Badge, Table, Modal, dll).

### Step 6: Define Component Responsibilities & State
Untuk tiap komponen:
- Purpose
- Expected Props / Inputs
- Local States & Global State dependencies
- Lifecycle / Status transitions (dari State Machine)

### Step 7: Map Data Dependencies
Petakan sumber data setiap komponen ke API endpoint (dari API Contract).

---

## Output

Simpan dokumen ke: `docs/ui-architecture/COMPONENT_MAP.md`
Setelah selesai: **"Langkah berikutnya: UI Slicing Document (aod-ui-slicing)"**
