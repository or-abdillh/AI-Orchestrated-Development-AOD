---
trigger: always_on
---

# AOD Architecture Engineering Guidelines — Project Rules

> **Status:** `Active (Dynamic Project Architecture Rules)`  
> **Trigger:** `always_on`  
> **Source Authority:** `docs/development/TECH_SPEC.md`  
> **Documentation Mirror:** `docs/development/ARCHITECTURE_ENGINEERING.md`  

---

## 1. Dynamic Project Architecture Overview

Aturan rekayasa arsitektur ini digenerate secara dinamis saat **Step 18 (`aod-tech-spec`)** dijalankan untuk mencerminkan keadaan riil, tech stack, dan konvensi spesifik proyek.

> [!IMPORTANT]
> **Dynamic Update Protocol:**
> Jika `docs/development/TECH_SPEC.md` telah disetujui, AI agent wajib memperbarui isi file ini mengikuti template `docs/samples/ARCHITECTURE_ENGINEERING_TEMPLATE.md` agar mencerminkan dependensi, direktori, dan konvensi eksak proyek saat ini.

---

## 2. Invariant Layering & Responsibility Boundaries (Universal)

Seluruh implementasi kode pada Phase 4 (Development) WAJIB mematuhi pemisahan tanggung jawab lapisan (*layer separation*):

1. **Controllers / Route Handlers (Thin Controllers):**
   - Hanya bertanggung jawab menerima HTTP request, memvalidasi input via FormRequest/DTO, mendelegasikan eksekusi ke Service/Action, dan mengembalikan response JSON/View.
   - ❌ **DILARANG:** Melakukan business logic, manipulasi perhitungan, atau pemanggilan query database langsung di dalam Controller.
2. **Services / Use Cases (Business Logic Core):**
   - Tempat seluruh business logic, aturan transaksi, dan kalkulasi berada.
   - Wajib membungkus operasi mutasi multi-tabel dalam Database Transaction (`DB::transaction`).
   - Menerima parameter primitif atau DTO/array tervalidasi, BUKAN HTTP Request object mentah.
3. **Models / Entities (Domain & Data Layer):**
   - Hanya mendefinisikan relasi, atribut casting, scopes, dan invariants entitas database.
   - Field dan tabel wajib 100% selaras dengan `docs/business/DATA_DICTIONARY.md`.
4. **Validation Layer (Dedicated Schemas):**
   - Setiap endpoint penerima input wajib memiliki FormRequest / Validator Schema terpisah. Dilarang inline validation di controller.
5. **Authorization Layer (Policies & Guards):**
   - Setiap mutasi atau pembacaan data privat wajib melewati Policy berbasis RBAC (`docs/business/RBAC.md`).

---

## 3. Visual & Design System Adherence (Frontends & Views)

Setiap kali agent menulis atau memodifikasi tampilan antarmuka (frontend components, Blade templates, views, CSS classes):
- **Otoritas Mutlak:** Wajib mematuhi `docs/system-design/DESIGN_SYSTEM.md` dan `docs/system-design/UI_STYLE.md`.
- **Zero Arbitrary Styling:** Dilarang menggunakan warna hex di luar token, arbitrary spacing (e.g. `p-[19px]`), atau komponen kustom yang melanggar hierarki atomik Design System.
- **State Handling:** Wajib menerapkan visual state matrix (hover, active, focus, disabled, loading skeleton, empty state, error banner) sesuai standar Design System.

---

## 4. Performance & Database Concurrency

- **Pemberantasan N+1 Query:** Eager loading (`with([...])`) wajib digunakan pada seluruh pemanggilan data relasi yang dirender atau diserialisasi.
- **Concurrency & Race Conditions:** Operasi pengurangan stok, pemotongan saldo, atau kuota wajib menggunakan row-level locking (`lockForUpdate`).
- **Database Schema Lockdown:** Dilarang menambahkan kolom atau tabel baru yang tidak tercatat di `docs/business/DATA_DICTIONARY.md`.

---

## 5. Definition of Done (DoD) Integration

Kode implementasi dianggap **DONE** hanya jika:
- [ ] Mematuhi struktur folder dan layer boundary pada file ini.
- [ ] Lolos seluruh kriteria pada `docs/development/DOD.md`.
- [ ] Memiliki automated tests (unit/feature) yang passing 100%.
- [ ] Dokumen referensi konteks (`docs/references/`) telah terbit dan terdaftar di `docs/references/INDEX.md`.
