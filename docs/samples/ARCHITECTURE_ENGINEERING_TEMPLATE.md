---
trigger: always_on
---

# Architecture Engineering Guidelines: [Project Name]

> **Version:** `v1.0.0`  
> **Last Updated:** `YYYY-MM-DD`  
> **Status:** `Active`  
> **Authority Source:** `docs/development/TECH_SPEC.md`  
> **Rule Scope:** Workspace Always-On (`.agents/rules/aod-architecture-engineering.md`)  
> **Framework:** AOD (AI-Orchestrated Development)  

---

## 1. System Invariants & Tech Stack

Daftar spesifikasi teknis dan dependensi resmi proyek yang telah diverifikasi melalui Context7 MCP:

| Komponen | Spesifikasi / Library | Versi | Standar / Konfigurasi Kunci |
|---|---|---|---|
| **Runtime & Language** | `[e.g. PHP 8.3 / Node.js 22 / Python 3.12]` | `vX.X` | Strict typing diaktifkan |
| **Core Framework** | `[e.g. Laravel 11 / Next.js 15 / FastAPI]` | `vX.X` | Standar MVC + Service Layer |
| **Database & Engine** | `[e.g. PostgreSQL 16 / MySQL 8.0]` | `vX.X` | InnoDB / pg_trgm, UUIDv7 / BigInt |
| **ORM / Query Builder** | `[e.g. Eloquent / Prisma / SQLAlchemy]` | `vX.X` | Eager loading wajib untuk cegah N+1 |
| **Authentication & IAM** | `[e.g. Laravel Sanctum / NextAuth / JWT]` | `vX.X` | Token expiry, refresh flow, RBAC policy |
| **Validation Engine** | `[e.g. FormRequest / Zod / Pydantic]` | `vX.X` | Dedicated schema layer |
| **Styling & Design System** | `[e.g. Tailwind CSS v4]` | `vX.X` | Kepatuhan mutlak `DESIGN_SYSTEM.md` |

---

## 2. Directory Structure & Layer Boundaries

Struktur folder fisik dan pemisahan tanggung jawab antarlayer:

```text
app/ (atau src/)
├── Models/ (atau entities/)         → Entitas, relasi, casts, dan domain invariants
├── Http/
│   ├── Controllers/                 → Thin controllers: delegasi ke Service, return response
│   ├── Requests/                    → Input validation ketat (FormRequest / Zod schema)
│   ├── Resources/ (atau serializers/) → Transformasi envelope output API
│   └── Middleware/                  → Auth check, tenant scoping, rate limiting
├── Services/ (atau use-cases/)      → Inti business logic, DB transactions, orchestrations
├── Policies/ (atau guards/)         → Otorisasi granular berbasis RBAC
├── Events/ & Listeners/             → Asynchronous side-effects (notifikasi, audit logs)
└── Exceptions/                      → Custom domain exceptions & handler
```

### Prohibited Cross-Layer Calls (Matriks Larangan Antarlayer)
- ❌ **Dilarang:** Controller melakukan query database langsung (`Model::where()`). Seluruh query harus melalui Service/Repository.
- ❌ **Dilarang:** Service mengakses HTTP Request object langsung (misal `$request->input()`). Kirimkan parameter primitif atau DTO/array tervalidasi ke Service.
- ❌ **Dilarang:** Business logic diletakkan di Model atau Controller. Model hanya untuk relasi, casts, dan scopes; Controller hanya untuk transport request/response.
- ❌ **Dilarang:** Raw SQL query tanpa parameter binding.

---

## 3. Naming & Syntax Conventions

Standar penamaan yang konsisten di seluruh lapisan kode:

| Elemen | Konvensi Penamaan | Contoh Nyata |
|---|---|---|
| **Class / Entity Model** | `PascalCase` (Singular) | `Order`, `ProductCategory`, `UserProfile` |
| **Database Table** | `snake_case` (Plural) | `orders`, `product_categories`, `users` |
| **Database Column** | `snake_case` (Eksak Data Dictionary) | `total_amount`, `paid_at`, `customer_id` |
| **Service Class** | `PascalCase` + `Service` suffix | `OrderCheckoutService`, `PaymentWebhookService` |
| **Controller Class** | `PascalCase` + `Controller` suffix | `OrderController`, `AuthController` |
| **Form Request / DTO** | `[Action][Entity]Request` | `StoreOrderRequest`, `UpdateProfileRequest` |
| **Policy Class** | `[Entity]Policy` | `OrderPolicy`, `ProductPolicy` |
| **Test File** | `[Subject]Test` | `OrderCheckoutTest.php`, `AuthServiceTest.ts` |
| **REST API Route** | `kebab-case` (Plural) | `/api/v1/product-categories`, `/api/v1/orders` |

---

## 4. Data Integrity, Concurrency & Transactions

1. **Multi-Table Operations:** Seluruh penulisan ke lebih dari 1 tabel **WAJIB** dibungkus dalam Database Transaction (`DB::transaction()` / `prisma.$transaction()`).
2. **Race Condition Prevention:** Modifikasi saldo, kuota, atau inventori stok wajib menggunakan row-level locking (`lockForUpdate` / optimistic lock).
3. **Idempotency:** Endpoint mutasi kritis (pembayaran, order submit) harus mendukung idempotency key untuk mencegah duplikasi eksekusi request.
4. **Soft Deletes:** Entitas bisnis utama wajib menerapkan soft deletes untuk integritas riwayat transaksi.

---

## 5. API Response Envelope & Exception Standards

Seluruh response API wajib mematuhi standar envelope seragam:

### Success Response (`200 OK` / `201 Created`)
```json
{
  "data": {
    "id": "ord-12345",
    "status": "pending_payment"
  },
  "meta": {
    "message": "Order successfully created",
    "timestamp": "2026-09-24T10:00:00Z"
  }
}
```

### Error Response (`400`, `401`, `403`, `404`, `422`, `500`)
```json
{
  "errors": {
    "code": "INSUFFICIENT_STOCK",
    "message": "Stok produk tidak mencukupi untuk jumlah yang diminta.",
    "details": [
      { "field": "items.0.quantity", "issue": "Requested 5, available 2" }
    ]
  },
  "meta": {
    "timestamp": "2026-09-24T10:00:00Z"
  }
}
```

---

## 6. Security & Authorization Protocol

1. **Authorization First:** Setiap aksi non-publik wajib diverifikasi menggunakan Policy/Guard sebelum business logic dijalankan.
2. **Input Sanitization:** Dilarang menggunakan `$request->all()` secara bebas. Hanya data yang lolos validasi `$request->validated()` yang boleh diproses.
3. **Sensitive Data Masking:** Password hash, API keys, dan token pihak ketiga tidak boleh dimasukkan ke dalam JSON response atau log.
4. **Query Performance:** Eager loading (`with(['items', 'user'])`) wajib digunakan saat mengakses relasi data untuk mencegah N+1 query.

---

## 7. Automated Testing Baseline & DoD Alignment

- **Test Suite Directory:** `tests/Feature/` untuk API & flow integration, `tests/Unit/` untuk pure service logic.
- **Passing Obligation:** Seluruh automated test wajib berstatus hijau (passing) sebelum kode di-commit.
- **Definition of Done Gate:** Setiap task implementasi wajib memvalidasi kepatuhan terhadap dokumen ini sebelum menyelesaikan DoD Pillar 2 (Code Architecture & Cleanliness).
