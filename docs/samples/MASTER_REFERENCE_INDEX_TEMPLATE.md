# Master Agent Reference Registry

> **Version:** `v1.0.0`  
> **Last Updated:** `YYYY-MM-DD`  
> **Status:** `Active`  
> **Framework:** AOD (AI-Orchestrated Development)  
> **Project Scope:** `[Nama Proyek / SME]`  
> **Active Git Branch:** `[branch-aktif]`  

---

## Revision History

| Version | Date | Author / Agent | Description |
|---|---|---|---|
| `v1.0.0` | YYYY-MM-DD | `aod-orchestrator` / `[agent-id]` | Inisialisasi Master Agent Reference Registry |

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

## 2. Phase 3: UI Slicing Reference Registry

Daftar seluruh halaman, view, dan komponen terpotong (*sliced UI components*) yang dihasilkan pada Phase 3:

| Ref ID | Halaman / Komponen | Target Route / Selector | File Komponen Utama | Dokumen Referensi | Git Branch | Status |
|---|---|---|---|---|---|---|
| `REF-UI-001` | Halaman Login | `/login` | `src/pages/auth/LoginPage.tsx` | [`REF-UI-auth-login.md`](docs/references/ui/REF-UI-auth-login.md) | `phase/03-ui-slicing` | `[✔] Sliced (Mock)` |
| `REF-UI-002` | Halaman Register | `/register` | `src/pages/auth/RegisterPage.tsx` | [`REF-UI-auth-register.md`](docs/references/ui/REF-UI-auth-register.md) | `phase/03-ui-slicing` | `[✔] Sliced (Mock)` |
| `REF-UI-003` | Order Checkout Page | `/checkout` | `src/pages/checkout/CheckoutPage.tsx` | [`REF-UI-orders-checkout.md`](docs/references/ui/REF-UI-orders-checkout.md) | `feat/ui-checkout` | `[⏳] In Progress` |

---

## 3. Phase 4: Feature Development Reference Registry

Daftar seluruh fitur teknis, service, dan business logic yang dihasilkan pada Phase 4:

| Ref ID | Modul | Fitur / Use Case | File Kode Kunci (Service/Controller) | Dokumen Referensi | Git Branch | Status |
|---|---|---|---|---|---|---|
| `REF-FEAT-001` | Auth | User Login & Token Issue | `app/Services/AuthService.php` | [`REF-FEAT-auth-login.md`](docs/references/features/REF-FEAT-auth-login.md) | `phase/00-setup` | `[✔] Completed` |
| `REF-FEAT-002` | Catalog | Master Product CRUD | `app/Services/ProductService.php` | [`REF-FEAT-catalog-products.md`](docs/references/features/REF-FEAT-catalog-products.md) | `phase/01-core` | `[✔] Completed` |
| `REF-FEAT-003` | Order | Checkout & Reservasi Stok | `app/Services/OrderCheckoutService.php` | [`REF-FEAT-orders-checkout.md`](docs/references/features/REF-FEAT-orders-checkout.md) | `feat/order-checkout` | `[⏳] In Progress` |

---

## 4. Cross-Reference & Integration Matrix (Traceability)

Matriks penghubung antara hasil Slicing UI (Phase 3) dengan Implementasi Backend/Feature (Phase 4):

| Modul / Sub-Modul | UI Reference | Feature Reference | Ref API Contract | Status Integrasi | Catatan Khusus |
|---|---|---|---|---|---|
| Auth / Login | `REF-UI-auth-login.md` | `REF-FEAT-auth-login.md` | `POST /api/v1/auth/login` | `[✔] Fully Integrated` | Selesai & lolos DoD |
| Order / Checkout | `REF-UI-orders-checkout.md` | `REF-FEAT-orders-checkout.md` | `POST /api/v1/orders/checkout` | `[⏳] Pending Binding` | Menunggu finalisasi webhook |

---

## 5. Agent Instructions for Updating this Registry

Setiap kali agent AI menyelesaikan step penulisan kode pada Phase 3 atau Phase 4:
1. **Identifikasi Kategori:** Tentukan apakah task merupakan penambahan UI baru, revisi UI, penambahan fitur backend, atau modifikasi logika.
2. **Tambah/Update Baris Tabel:** Tambahkan baris baru pada tabel Seksi 2, 3, atau 4 dengan format tautan relatif ke dokumen referensi di `docs/references/ui/` atau `docs/references/features/`.
3. **Perbarui Hierarchy Tree:** Jika terdapat modul atau sub-modul baru, tambahkan cabang pada Seksi 1.
4. **Naikkan Versi (SemVer):** Naikkan versi patch/minor pada header dokumen dan catat di tabel `Revision History`.
5. **Commit Bersama Kode:** Pastikan perubahan file ini di-stage dan di-commit bersamaan dengan kode dan file referensi terkait.
