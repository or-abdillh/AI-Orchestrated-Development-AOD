# Agent Reference Context: [Feature Name]

> **Reference ID:** `REF-FEAT-[module]-[slug]`  
> **Version:** `v1.0.0`  
> **Last Updated:** `YYYY-MM-DD`  
> **Status:** `Completed` *(Planned / In Progress / Completed / Deprecated)*  
> **Module / Sub-module:** `[Module Name]` / `[Sub-module Name]`  
> **Phase Target:** Phase [N] — [Phase Name]  
> **Author / Agent:** `aod-feature-prompts` / `[agent-id]`  
> **Git Branch:** `feat/[module]-[slug]`  
> **Latest Commit:** `[commit-hash]`  
> **Upstream Specs:**  
> - PRD: `docs/business/PRD.md#section-[num]`  
> - Tech Spec: `docs/development/TECH_SPEC.md#module-[name]`  
> - Data Dictionary: `docs/business/DATA_DICTIONARY.md#table-[name]`  
> - API Contract: `docs/system-design/API_CONTRACT.md#[endpoint]`  
> - State Machine: `docs/system-design/STATE_MACHINE.md#[entity]`  
> - UI Reference: `docs/references/ui/REF-UI-[slug].md` *(jika ada UI terkait)*  

---

## Revision History

| Version | Date | Author / Agent | Description |
|---|---|---|---|
| `v1.0.0` | YYYY-MM-DD | `aod-feature-prompts` | Initial feature implementation and architectural documentation |

---

## 1. Architectural Footprint (Physical Code Manifest)

Daftar seluruh file fisik yang diciptakan atau dimodifikasi selama implementasi fitur ini:

| Layer / Kategori | Path File | Peran / Deskripsi Tanggung Jawab |
|---|---|---|
| **Database Migration** | `database/migrations/2026_09_24_000001_create_orders_table.php` | Skema tabel `orders` & `order_items`, foreign keys, dan index |
| **Model / Entity** | `app/Models/Order.php` | Definisi relasi (`items`, `user`), casting tipe, dan scope query |
| **Request Validation** | `app/Http/Requests/CheckoutOrderRequest.php` | Validasi payload input ketat (tipe, regex, exists, enum) |
| **Business Service** | `app/Services/OrderCheckoutService.php` | Inti logika bisnis: kalkulasi harga, diskon, reservasi stok, DB transaction |
| **Controller** | `app/Http/Controllers/Api/OrderController.php` | Controller tipis: delegasi request ke Service dan bungkus API Resource |
| **API Resource** | `app/Http/Resources/OrderResource.php` | Transformasi output response sesuai format standar AOD |
| **Authorization Policy** | `app/Policies/OrderPolicy.php` | Pembatasan akses RBAC (hanya pemilik order atau role admin yang berhak) |
| **Events & Listeners** | `app/Events/OrderCreated.php` | Dispatch event asynchronous setelah order berhasil dibuat |
| **Automated Tests** | `tests/Feature/OrderCheckoutTest.php` | Test suite happy path, out-of-stock validation, dan unauthorized check |

---

## 2. Request Lifecycle & Business Invariants

### Alur Eksekusi Permintaan (Request Lifecycle)
1. **Route & Middleware:** Endpoint dilindungi middleware `auth:sanctum` dan `throttle:60,1`.
2. **Validation Layer:** `CheckoutOrderRequest` memvalidasi ketersediaan `address_id` dan minimal 1 item belanja.
3. **Authorization Check:** Policy memastikan akun pengguna aktif dan tidak sedang disuspend.
4. **Service Transaction:** `OrderCheckoutService::execute()` dijalankan dalam blok `DB::transaction()`:
   - Verifikasi kuantiti stok produk (eager loading dengan row lock: `lockForUpdate`).
   - Kurangi stok fisik produk pada tabel `products`.
   - Simpan record `orders` dan `order_items`.
5. **Event Emission:** Memicu event `OrderCreated` (dispatched setelah commit transaksi berhasil).
6. **Response Wrapping:** Mengembalikan HTTP `201 Created` dibungkus format envelope standar `{ data, meta }`.

### Business Invariants (Aturan Mutlak yang Dijaga)
- **Zero Overselling:** Stok produk wajib diverifikasi sebelum pengurangan; jika stok tidak mencukupi, transaksi otomatis rollback dengan exception `InsufficientStockException`.
- **Atomic Checkout:** Jika gagal menyimpan record `order_items`, order induk tidak boleh terbentuk.
- **Thin Controller:** Controller dilarang melakukan query database langsung atau manipulasi perhitungan uang.

---

## 3. API Contract & Data Mapping

- **HTTP Method & Route:** `POST /api/v1/orders/checkout`
- **Request Headers:** `Authorization: Bearer <token>`, `Accept: application/json`

### Example Request Body
```json
{
  "address_id": "addr-992",
  "payment_method": "bank_transfer",
  "items": [
    {
      "product_id": "prod-101",
      "quantity": 2
    }
  ]
}
```

### Example Response Body (`201 Created`)
```json
{
  "data": {
    "order_id": "ord-8831",
    "order_number": "INV/20260924/001",
    "total_amount": 3700000,
    "status": "pending_payment",
    "created_at": "2026-09-24T10:00:00Z"
  },
  "meta": {
    "message": "Order successfully created"
  }
}
```

---

## 4. State Machine Compliance & Transitions

Entitas `Order` mematuhi `docs/system-design/STATE_MACHINE.md`:
- **Initial State:** `pending_payment`
- **Allowed Next States:** `paid` (via webhook/payment confirmation), `cancelled` (via timeout/user).
- **Prevented States:** Transisi langsung dari `pending_payment` ke `completed` dilarang oleh guard method `Order::canTransitionTo()`.

---

## 5. Automated Testing & Verification Evidence

- **Test Suite:** `tests/Feature/OrderCheckoutTest.php`
- **Test Command:**
  ```bash
  php artisan test --filter=OrderCheckoutTest
  ```
- **Hasil Verifikasi:**
  - `test_user_can_successfully_checkout_with_valid_items` -> **PASSED**
  - `test_checkout_fails_when_product_stock_is_insufficient` -> **PASSED**
  - `test_unauthenticated_user_cannot_checkout` -> **PASSED**
- **DoD Compliance:** Seluruh 6 kriteria fungsional, keamanan, arsitektur, dan pilar ke-7 (ARC) telah terverifikasi penuh.

---

## 6. Agent Continuity & Maintenance Guide

Panduan bagi AI agent berikutnya yang akan memodifikasi modul ini:

> [!WARNING]
> **Perhatian Khusus Transaksi & Concurrency:**
> - Selalu pertahankan `DB::transaction()` dan locking row pada saat memanipulasi stok produk di `OrderCheckoutService`.
> - Jika ada kebutuhan menambahkan voucher/diskon, masukkan logic pada `DiscountCalculatorService` terpisah dan inject ke `OrderCheckoutService` agar SRP (Single Responsibility Principle) tetap terjaga.
> - Jika ada integrasi notifikasi baru, daftarkan listener baru pada event `OrderCreated` tanpa memodifikasi service utama checkout.
