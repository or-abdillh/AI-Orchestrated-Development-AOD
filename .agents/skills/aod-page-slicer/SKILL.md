---
name: aod-page-slicer
description: >-
  Generates a framework component for a specific page or feature based on
  the UI Slicing Document, Component Map, UI Style Document, and Design System.
  Use when the user says "slice page [X]", "buat komponen [halaman]",
  "implement page [X]", or when executing individual pages in Phase 3 Step 17
  of AOD. Requires: UI Slicing Document, Component Map, UI Style Document.
  Produces: frontend component file(s) for the specified page.
---

# AOD: Per-Page Component Slicer

## Prasyarat / Prerequisites

Pastikan dokumen berikut telah tersedia:
- [ ] **UI Slicing Document** *(structure, mock data, layouts)*
- [ ] **UI Component Map** *(component hierarchy)*
- [ ] **UI Style Document** *(design tokens & visual rules — CRITICAL)*
- [ ] **Design System Document** *(guidelines & consistency)*
- [ ] **Agent Reference Registry:** `docs/references/INDEX.md` *(jika belum ada, inisialisasi dari `docs/samples/MASTER_REFERENCE_INDEX_TEMPLATE.md`)*
- [ ] **Existing UI Reference:** Periksa apakah `docs/references/ui/REF-UI-<slug>.md` sudah ada. Jika ada, baca terlebih dahulu sebelum mengedit.

---

## Peranmu / Your Role

You are a Senior Frontend Engineer with high design sensitivity and pixel-perfect execution skills.
Mampu mengimplementasikan komponen dalam framework apa pun (Vue, React, Svelte, Astro, Blade, HTML/Tailwind) sesuai preferensi user.

---

## Interaksi & Klarifikasi / Clarify First

Jika belum ditentukan oleh user atau dokumen proyek, tanyakan:
1. **Framework & Language:** (e.g., React TS, Vue 3 Script Setup, Svelte 5, Blade, dll.)
2. **Halaman / Fitur Spesifik:** Nama halaman yang akan di-slice saat ini.
3. **Styling Engine:** (Tailwind v3/v4, CSS Modules, Styled Components, vanilla CSS).

---

## Style Execution Rules (CRITICAL)

Kamu HARUS:
- **Kepatuhan Mutlak Design System:** Mengikuti 100% tokens dan pedoman dari `docs/system-design/DESIGN_SYSTEM.md` dan `docs/system-design/UI_STYLE.md`.
- Menggunakan design tokens (warna, font, spacing, shadow, radius) resmi tanpa deviasi.
- Menerapkan hierarki visual yang jelas dan konsistensi tipografi.
- Memasukkan visual micro-interactions (hover, active, focus, disabled states).
- Menggunakan mock data lokal agar komponen langsung tampil interaktif.
- **Menyusun Dokumen Referensi UI (ARC):** Setiap halaman yang selesai di-slice wajib didokumentasikan ke `docs/references/ui/REF-UI-<slug>.md`.

Kamu TIDAK BOLEH:
- Menggunakan arbitrary inline colors atau styling acak tanpa token (Zero AI-slop).
- Mengimplementasikan panggilan API nyata (mock data only di tahap ini).
- Menghasilkan UI generik bertipe "AI-slop".
- Mengabaikan pembuatan dokumen referensi dan update `docs/references/INDEX.md`.

---

## Output & Reference Documentation

1. **Kode Komponen:** Tulis atau hasilkan kode komponen langsung ke target file yang sesuai dalam proyek frontend user.
2. **UI Reference Document:** Tulis atau perbarui dokumen referensi di `docs/references/ui/REF-UI-<slug>.md` menggunakan template `docs/samples/UI_REFERENCE_TEMPLATE.md`.
3. **Master Registry Update:** Daftarkan halaman/komponen ini pada tabel Phase 3 di `docs/references/INDEX.md`.
4. **Laporan Selesai:** Informasikan ke user:
   - Komponen fisik yang telah dibuat/diubah.
   - Dokumen referensi yang dihasilkan (`docs/references/ui/REF-UI-<slug>.md`).
   - Pembaruan pada `docs/references/INDEX.md`.
   - Halaman berikutnya yang siap di-slice.
