# Agent Reference Context: [Page / Component Name]

<!-- arc:metadata:start -->
```json
{
  "schema_version": 1,
  "id": "REF-UI-module-page",
  "title": "Replace with actual feature/page title",
  "type": "ui",
  "module_id": "replace-module-id",
  "feature_id": "replace-feature-id",
  "status": "draft",
  "updated_at": "YYYY-MM-DD",
  "tags": [],
  "sources": [],
  "related_refs": [],
  "code_paths": []
}
```
<!-- arc:metadata:end -->

Metadata di atas adalah placeholder, bukan referensi proyek yang sudah terdaftar.
Ganti dengan identitas dan hubungan aktual sebelum menyimpan di docs/references/.
ID pada header dan INDEX harus sama dengan metadata. Path metadata relatif ke
root proyek; fragment dokumen disimpan terpisah. Gunakan sources untuk dokumen
sumber, related_refs untuk koneksi ARC, dan code_paths untuk file aktual.
Contoh source: {"path":"docs/business/PRD.md","fragment":"equipment","relation":"implements"}.
Contoh related_refs: {"id":"REF-FEAT-equipment-create","relation":"integrates_with"}.
Status metadata menyatakan kondisi referensi, bukan bukti test lulus atau UAT diterima.
Koneksi metadata hanya deklarasi, bukan hasil verifikasi semantik otomatis.


> **Reference ID:** `REF-UI-[slug]`
> **Version:** `v1.1.0`
> **Last Updated:** `2026-11-05`
> **Status:** `Draft` *(Draft / Active / Deprecated — status dokumen referensi)*
> **Author / Agent:** `aod-page-slicer` / `[agent-id]`
> **Target Route:** `/path/to/page`
> **Primary Layout:** `[AppLayout / AuthLayout / DashboardLayout]`
> **Framework & Engine:** `[e.g. Next.js 15 / React 19 / Tailwind CSS v4]`
> **Git Branch:** `feat/ui-[slug]` *(or current branch)*
> **Upstream Specs:**
> - UI Flow: `docs/system-design/UI_FLOW.md#screen-[id]`
> - Component Map: `docs/ui-architecture/COMPONENT_MAP.md#[section]`
> - UI Style Doc: `docs/system-design/UI_STYLE.md`
> - API Contract: `docs/system-design/API_CONTRACT.md#[endpoint]`

---

## Revision History

| Version | Date | Author / Agent | Description |
|---|---|---|---|
| `v1.1.0` | 2026-11-05 | AOD | Structured ARC metadata, stable identity and CLI navigation contract |
| `v1.0.1` | 2026-11-02 | `aod-page-slicer` | Initial UI slicing and component documentation |

---

## 1. Architectural Overview & Component Hierarchy

Peta hierarki komponen terpotong (*component tree*) dari level layout hingga atom:

```text
[Page: OrderCheckoutPage.tsx]
├── [Layout: DashboardLayout]
│   └── Header & Breadcrumbs
├── [Organism: CartSummaryTable]
│   ├── [Molecule: CartItemRow] (repeatable)
│   │   ├── [Atom: QuantityCounter]
│   │   └── [Atom: PriceTag]
│   └── [Molecule: OrderSummaryTotal]
├── [Organism: ShippingAddressSelector]
│   └── [Molecule: AddressCard] (radio selection)
└── [Organism: PaymentMethodPicker]
    ├── [Molecule: PaymentOptionRadio]
    └── [Atom: SubmitOrderButton]
```

### Physical Files Generated / Modified
- `src/pages/checkout/CheckoutPage.tsx` — Main page wrapper and layout binding
- `src/components/checkout/CartSummaryTable.tsx` — Table component for items
- `src/components/checkout/ShippingAddressSelector.tsx` — Address selection card
- `src/mocks/checkoutMockData.ts` — Local mock data dataset

---

## 2. Visual Design & Design Token Compliance

Daftar tokens dari `docs/system-design/UI_STYLE.md` yang diterapkan secara ketat:

| Elemen Visual | Token / Class Utility | Catatan Tampilan |
|---|---|---|
| **Color: Primary Action** | `bg-primary-600 hover:bg-primary-700` | Tombol CTA utama Checkout |
| **Color: Status Badges** | `bg-amber-100 text-amber-800` (Pending), `bg-emerald-100 text-emerald-800` (Paid) | Sesuai State Machine |
| **Typography: Headings** | `font-display text-2xl font-bold tracking-tight` | Header halaman checkout |
| **Spacing & Padding** | `p-6 md:p-8 space-y-6` | Konsistensi grid 8px |
| **Radius & Shadow** | `rounded-xl shadow-sm border border-slate-200` | Card container |

### Responsive & Layout Behavior
- **Mobile (`< 768px`):** Single column vertical stack, sticky checkout button at the bottom.
- **Desktop (`>= 768px`):** 2-column layout (Left: Shipping & Payment, Right: Sticky Cart Summary).

---

## 3. Mock Data Schema & UI State Mapping

### Local Mock Schema (`src/mocks/[mockFile].ts`)
```typescript
export interface CheckoutMockItem {
  id: string;
  name: string;
  price: number;
  qty: number;
  imageUrl: string;
}

export const mockCheckoutItems: CheckoutMockItem[] = [
  {
    id: "prod-001",
    name: "Premium Ergonomic Chair",
    price: 1850000,
    qty: 1,
    imageUrl: "/images/products/chair.webp",
  },
];
```

### Visual State Mapping (State Machine Compliance)
| UI State | Komponen / Tampilan | Bukti Penanganan |
|---|---|---|
| **Loading State** | Skeleton shimmer placeholder | `SkeletonCard.tsx` dirender saat `isLoading = true` |
| **Empty State** | Ilustrasi cart kosong + tombol "Kembali Belanja" | `EmptyCartNotice.tsx` saat `items.length === 0` |
| **Error State** | Banner peringatan merah + tombol retry | Alert message saat simulasi gagal kalkulasi ongkir |
| **Success State** | Modal konfirmasi order terkirim | Dialog pop-up menuju `/order-success` |

---

## 4. Interactive Behaviors & Client-Side State

- **Local State Handling:** Menggunakan `useState` / signal untuk mengontrol seleksi metode bayar, jumlah kuantiti produk, dan aktivasi tab.
- **Micro-interactions:** Hover highlight pada kartu alamat yang dapat dipilih, ripple effect pada tombol bayar.
- **Client Validation:** Tombol checkout disabled jika belum ada alamat pengiriman yang dipilih.

---

## 5. Phase 4 Backend Integration Hooks (Handoff Guide)

Bagian ini dirancang agar agent Phase 4 (Feature Development) dapat langsung menghubungkan backend API tanpa perlu menduga-duga props:

### Props & Data Binding Points
- Ganti import `mockCheckoutItems` dengan hook/query data riil dari API (`useCartQuery` / server component fetch).
- **Target Endpoint API:** `POST /api/v1/orders/checkout` (lihat `docs/system-design/API_CONTRACT.md#orders-checkout`).

### Payload Mapping
Data lokal yang siap dikirim ke backend API:
```json
{
  "address_id": "addr-123",
  "payment_method": "bank_transfer",
  "items": [
    { "product_id": "prod-001", "quantity": 1 }
  ]
}
```

---

## 6. Agent Continuity & Maintenance Guide

Instruksi bagi AI agent berikutnya yang akan memodifikasi atau memperluas halaman ini:

> [!TIP]
> **Panduan Modifikasi Komponen:**
> - Jika ingin menambahkan metode pembayaran baru, tambahkan tipe pada `PaymentMethodPicker.tsx` dan pastikan ikon SVG tersedia di `src/assets/icons/`.
> - Komponen `CartSummaryTable` bersifat reusable; jika digunakan di halaman Order Detail, kirimkan prop `isReadOnly={true}` untuk menyembunyikan aksi penambahan kuantiti.
> - Hindari mengubah padding luar kontainer halaman agar tidak bertabrakan dengan `DashboardLayout`.

> Template revision v1.1.0 (2026-11-05): structured ARC metadata and CLI navigation; examples remain illustrative.
> All sample routes, framework tokens, statuses and test results above are illustrative.
> Replace with actual project evidence; examples never prove completion or approval.
