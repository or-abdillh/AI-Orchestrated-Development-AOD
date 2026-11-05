# Master Agent Reference Registry

> **Version:** `v1.1.0`
> **Last Updated:** `2026-11-05`
> **Status:** `Active`
> **Framework:** AOD (AI-Orchestrated Development)
> **Project Scope:** `[Nama Proyek / SME]`
> **Active Git Branch:** `[branch-aktif]`

---

## Revision History

| Version | Date | Author / Agent | Description |
|---|---|---|---|
| `v1.1.0` | 2026-11-05 | AOD | Structured ARC metadata, stable identity and CLI navigation contract |
| `v1.0.1` | 2026-11-02 | `aod-orchestrator` / `[agent-id]` | Inisialisasi Master Agent Reference Registry |

---

## 1. Module & Capability Hierarchy

Peta navigasi hierarki modul, sub-modul, dan kapabilitas sistem sebagai panduan orientasi cepat bagi AI agent:

```text
Project Root/
├── [Module A: e.g. Auth & IAM]
│   ├── Sub-module: Login & Session
│   │   ├── UI: Login Page (`REF-UI-auth-login.md`)
│   │   └── Feature: Session Service & JWT (`REF-FEAT-auth-session.md`)
│   └── Sub-module: Registration & Email Verification
│       ├── UI: Register Page (`REF-UI-auth-register.md`)
│       └── Feature: User Registration Action (`REF-FEAT-auth-register.md`)
├── [Module B: e.g. Catalog & Inventory]
│   ├── Sub-module: Product Management
│   │   ├── UI: Product List & Detail (`REF-UI-catalog-products.md`)
│   │   └── Feature: Product CRUD & Stock Service (`REF-FEAT-catalog-products.md`)
└── [Module C: e.g. Order Processing]
    ├── Sub-module: Checkout & Cart
    │   ├── UI: Cart Drawer & Checkout Screen (`REF-UI-orders-checkout.md`)
    │   └── Feature: Order Creation & Stock Lock (`REF-FEAT-orders-checkout.md`)
```

---

## 2. Phase 4: UI Page Implementation Reference Registry

Daftar seluruh halaman, view, dan komponen terpotong (*sliced UI components*) yang dihasilkan pada Phase 4:

| Ref ID | Halaman / Komponen | Target Route / Selector | File Komponen Utama | Dokumen Referensi | Git Branch | Status |
|---|---|---|---|---|---|---|
| `REF-UI-auth-login` | Halaman Login | `/login` | `src/pages/auth/LoginPage.tsx` | [`REF-UI-auth-login.md`](ui/REF-UI-auth-login.md) | `feat/ui-slicing` | `[✔] Sliced (Mock)` |
| `REF-UI-auth-register` | Halaman Register | `/register` | `src/pages/auth/RegisterPage.tsx` | [`REF-UI-auth-register.md`](ui/REF-UI-auth-register.md) | `feat/ui-slicing` | `[✔] Sliced (Mock)` |
| `REF-UI-orders-checkout` | Order Checkout Page | `/checkout` | `src/pages/checkout/CheckoutPage.tsx` | [`REF-UI-orders-checkout.md`](ui/REF-UI-orders-checkout.md) | `feat/ui-checkout` | `[⏳] In Progress` |

---

## 3. Phase 4: Feature Development Reference Registry

Daftar seluruh fitur teknis, service, dan business logic yang dihasilkan pada Phase 4:

| Ref ID | Modul | Fitur / Use Case | File Kode Kunci (Service/Controller) | Dokumen Referensi | Git Branch | Status |
|---|---|---|---|---|---|---|
| `REF-FEAT-auth-login` | Auth | User Login & Token Issue | `app/Services/AuthService.php` | [`REF-FEAT-auth-login.md`](features/REF-FEAT-auth-login.md) | `phase/00-setup` | `[✔] Completed` |
| `REF-FEAT-catalog-products` | Catalog | Master Product CRUD | `app/Services/ProductService.php` | [`REF-FEAT-catalog-products.md`](features/REF-FEAT-catalog-products.md) | `phase/01-core` | `[✔] Completed` |
| `REF-FEAT-orders-checkout` | Order | Checkout & Reservasi Stok | `app/Services/OrderCheckoutService.php` | [`REF-FEAT-orders-checkout.md`](features/REF-FEAT-orders-checkout.md) | `feat/order-checkout` | `[⏳] In Progress` |

---

## 4. Cross-Reference & Integration Matrix (Traceability)

Matriks penghubung antara hasil Slicing UI (Phase 3) dengan Implementasi Backend/Feature (Phase 4):

| Modul / Sub-Modul | UI Reference | Feature Reference | Ref API Contract | Status Integrasi | Catatan Khusus |
|---|---|---|---|---|---|
| Auth / Login | `REF-UI-auth-login.md` | `REF-FEAT-auth-login.md` | `POST /api/v1/auth/login` | `[✔] Fully Integrated` | Selesai & lolos DoD |
| Order / Checkout | `REF-UI-orders-checkout.md` | `REF-FEAT-orders-checkout.md` | `POST /api/v1/orders/checkout` | `[⏳] Pending Binding` | Menunggu finalisasi webhook |

---

## 5. Agent Instructions for Updating this Registry

Setelah perubahan implementasi terkait pada Phase 4 atau scoped change:
1. **Identifikasi Kategori:** Tentukan apakah task merupakan penambahan UI baru, revisi UI, penambahan fitur backend, atau modifikasi logika.
2. **Tambah/Update Baris Tabel:** Tambahkan baris baru pada tabel Seksi 2, 3, atau 4 dengan format tautan relatif ke dokumen referensi di `docs/references/ui/` atau `docs/references/features/`.
3. **Perbarui Hierarchy Tree:** Jika terdapat modul atau sub-modul baru, tambahkan cabang pada Seksi 1.
4. **Naikkan Versi (SemVer):** Naikkan versi patch/minor pada header dokumen dan catat di tabel `Revision History`.
5. **Commit Bersama Kode:** Pastikan perubahan file ini di-stage dan di-commit bersamaan dengan kode dan file referensi terkait.

> Template revision v1.1.0 (2026-11-05): structured ARC metadata and CLI navigation; examples remain illustrative.
> All sample routes, framework tokens, statuses and test results above are illustrative.
> Replace with actual project evidence; examples never prove completion or approval.

## CLI ARC

Gunakan `./.agents/aod/bin/arc list` untuk referensi terdaftar dan `list --all`
untuk menemukan referensi yang belum terdaftar. `check` menampilkan entri hilang,
ID duplikat dan metadata legacy. Registry tetap menjadi sumber membership;
identitas dan koneksi berasal dari metadata dokumen ARC. CLI tidak mengubah
registry atau referensi secara otomatis. Isi tabel ini harus memakai ID aktual
yang sama dengan metadata, bukan nomor urut tampilan.
