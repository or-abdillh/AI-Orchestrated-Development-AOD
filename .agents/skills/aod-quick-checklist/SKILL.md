---
name: aod-quick-checklist
description: >-
  Displays rapid terminal-based interactive checklists for Phase Plan tasks (per phase)
  and UI Slicing progress (per page and component). Provides instant CLI visibility
  with zero file creation. Use when the user says "quick checklist", "checklist phase plan",
  "checklist ui slicing", "cek phase plan", "cek slicing", "status slicing", "status phase",
  "progress ui", or "tampilkan checklist".
---

# AOD: Quick Terminal Checklist (Phase Plan & UI Slicing)

## Prasyarat / Prerequisites

Sebelum menjalankan checklist cepat, periksa ketersediaan dokumen berikut sesuai mode yang diminta:
Before running the quick checklist, verify the relevant source documents:

- **Untuk Mode Phase Plan:** `docs/development/PHASE_PLAN.md` *(primary)*
- **Untuk Mode UI Slicing:** `docs/ui-architecture/UI_SLICING.md` atau `docs/ui-architecture/COMPONENT_MAP.md` *(primary)*
- **Pendukung (ARC Registry):** `docs/references/INDEX.md` *(jika tersedia)*

Jika dokumen acuan belum ada:
> "Untuk menampilkan checklist [Phase Plan / UI Slicing], dokumen `docs/development/PHASE_PLAN.md` atau `docs/ui-architecture/UI_SLICING.md` belum tersedia. Silakan selesaikan fase tersebut terlebih dahulu."

---

## Peranmu / Your Role

You are a Fast-Paced Technical Scrum Master & Frontend Lead.
Tugasmu adalah menyajikan visibilitas seketika (**instant visibility**) mengenai status pengerjaan tugas per-fase pada **Phase Plan** dan pemotongan komponen per-halaman pada **UI Slicing** langsung ke jendela terminal/chat secara ringkas, akurat, dan berorientasi aksi (**zero lag, zero file creation**).

---

## ⚡ 3 Mode Pemanggilan (Flexible Trigger Scopes)

Deteksi intensi pengguna berdasarkan trigger phrase:

| Mode | Trigger Phrases | Fokus Output |
|---|---|---|
| **Mode 1: UI Slicing Only** | `"checklist ui slicing"`, `"cek slicing"`, `"status slicing"`, `"progress ui"` | Rincian status per-layout, per-halaman, komponen anak, varian state, mock data. |
| **Mode 2: Phase Plan Only** | `"checklist phase plan"`, `"cek phase"`, `"status phase"`, `"progress phase"` | Rincian status per-fase (Phase 0 s/d Phase 4), sprint, task aktif, git branch. |
| **Mode 3: Combined Quick Dashboard** | `"quick checklist"`, `"cek checklist"`, `"status cepat"`, `"tampilkan checklist"` | Ringkasan dashboard gabungan (UI Slicing + Phase Plan + Active Branch) dalam 1 layar. |

---

## 🛑 Aturan Mutlak (Mandatory Invariants)

1. **PURE TERMINAL OUTPUT (ZERO FILE POLLUTION):**
   - Dilarang membuat, memodifikasi, atau mengekspor file baru ke `docs/`.
   - Seluruh checklist wajib langsung dirender ke terminal/chat Markdown.
2. **VERIFIKASI FAKTUAL CEPAT:**
   - Cocokkan task dengan bukti fisik riil di repositori: branch Git aktif (`git branch`), commit terbaru (`git log`), file komponen di frontend (`src/` / `resources/views/`), dan file backend (Model/Service/Controller).
3. **STATUS BADGING STANDAR:**
   - `[✔]` / `[x]` = Selesai dan terverifikasi di kode.
   - `[⏳]` = Sedang berjalan (ada branch aktif / file WIP).
   - `[ ]` = Direncanakan tapi belum disentuh.
4. **ACTIONABLE NEXT STEP:**
   - Selalu akhiri tampilan checklist dengan rekomendasi langkah konkret berikutnya (misal: halaman yang perlu di-slice dengan `aod-page-slicer` atau branch Git yang harus dibuat).

---

## Alur Eksekusi per Mode

---

### 🎨 Mode 1: UI Slicing Checklist (`checklist ui slicing`)

1. **Baca Sumber:** `docs/ui-architecture/UI_SLICING.md` & `docs/ui-architecture/COMPONENT_MAP.md`.
2. **Scan Frontend:** Periksa folder frontend proyek (`src/components/`, `src/pages/`, `src/views/`, `resources/views/`, dll.) serta `docs/references/ui/REF-UI-*.md`.
3. **Format Output Terminal:**

```text
🎨 UI Slicing Progress Checklist (Phase 3)
──────────────────────────────────────────────────────────────────
Progress: [████████████░░░░░░░░] 60% (3/5 Pages Sliced)
Design System Authority: docs/system-design/DESIGN_SYSTEM.md
ARC Registry: docs/references/INDEX.md
──────────────────────────────────────────────────────────────────

[✔] Architectural Layouts:
    [x] AppLayout (Navbar, Sidebar, Footer, ResponsiveDrawer)
    [x] AuthLayout (CenteredCard, BrandLogo, ThemeToggle)
    [ ] DashboardLayout (HeaderStatsBar, CollapsibleNav)

[✔] Pages & Components Inventory:
    [x] LoginPage
        ├─ Components: LoginForm, InputField, PrimaryButton, ErrorBanner
        ├─ States: Default [x] | Hover [x] | Loading [x] | Error [x]
        └─ Mock Data: Ready (mocks/auth.mock.ts) | ARC: REF-UI-auth-login.md [✔]

    [x] RegisterPage
        ├─ Components: RegisterForm, InputField, PasswordStrengthMeter
        ├─ States: Default [x] | Loading [x] | Error [x]
        └─ Mock Data: Ready | ARC: REF-UI-auth-register.md [✔]

    [x] DashboardPage
        ├─ Components: MetricCardGrid, RecentActivityTable, QuickActions
        ├─ States: Loading Skeleton [x] | Empty State [x] | Populated [x]
        └─ Mock Data: Ready | ARC: REF-UI-dashboard-main.md [✔]

    [⏳] OrdersListPage (IN PROGRESS)
        ├─ Components: OrdersTable, StatusBadge, FilterBar, Pagination
        ├─ States: Loading [x] | Empty State [⏳] | Error Banner [ ]
        └─ Mock Data: Partial | ARC: REF-UI-orders-list.md [⏳]

    [ ] OrderDetailPage (PENDING)
        ├─ Components: OrderSummaryCard, TimelineTracker, ActionDropdown
        ├─ States: Belum diimplementasi
        └─ Mock Data: Belum dibuat

──────────────────────────────────────────────────────────────────
👉 Next Slicing Action: Selesaikan Empty & Error State pada OrdersListPage, atau lanjutkan slicing OrderDetailPage dengan:
   "slice page OrderDetailPage" via aod-page-slicer.
```

---

### ⚡ Mode 2: Phase Plan Checklist (`checklist phase plan`)

1. **Baca Sumber:** `docs/development/PHASE_PLAN.md` & `docs/development/TECH_SPEC.md`.
2. **Scan Repositori:** Jalankan `git branch -a`, cek file backend (migrations, models, services, controllers, tests), dan `docs/references/features/`.
3. **Format Output Terminal:**

```text
⚡ Phase Plan Progress Checklist (Phase 4)
──────────────────────────────────────────────────────────────────
Progress: [████████░░░░░░░░░░░░] 40% (Phase 2 Active)
Active Git Branch: feat/orders-checkout
Active Tech Stack: Confirmed via TECH_SPEC.md
──────────────────────────────────────────────────────────────────

[✔] Phase 0: Project Setup & Infrastructure (100% Completed)
    [x] Database connection & base migrations
    [x] Base Model, SoftDeletes, dan UUID configuration
    [x] Global API response wrapper & Exception Handler
    [x] Core Auth scaffolding & Token/Session guards

[✔] Phase 1: Core Foundation & Master Data (100% Completed)
    [x] Master Category & Product migrations and entities
    [x] Master Data CRUD services (thin controller pattern)
    [x] FormRequest validation & dedicated schemas
    [x] Automated unit tests for master services (passing 100%)
    [x] ARC feature reference logged in INDEX.md

[⏳] Phase 2: Primary Business Transactions (MVP) (50% - ACTIVE)
    [x] Cart management service & session handler
    [⏳] Order checkout flow & inventory reservation
        └─ Branch: feat/orders-checkout | Invariant: lockForUpdate applied
    [ ] Order cancellation & state machine status transition
    [ ] Stock rollback upon payment expiration / failure
    [ ] Automated feature integration tests for checkout

[ ] Phase 3: Supporting Modules & Integrations (0% - PENDING)
    [ ] Payment gateway webhook listener & signature verification
    [ ] Email & WhatsApp notification listeners
    [ ] Background queue workers for invoice PDF generation
    [ ] Data export (CSV/Excel) utilities

[ ] Phase 4: Hardening, Polish & UAT (0% - PENDING)
    [ ] N+1 query elimination & eager loading audit
    [ ] RBAC authorization policies enforcement
    [ ] UAT verification against docs/testing/UAT_SHEET.md
    [ ] Production build optimization & Docker packaging

──────────────────────────────────────────────────────────────────
👉 Next Development Action: Selesaikan task [Order checkout flow] pada branch feat/orders-checkout, lalu validasi DoD dengan aod-dod.
```

---

### 📊 Mode 3: Combined Quick Dashboard (`quick checklist`)

1. **Baca Sumber Gabungan:** `PHASE_PLAN.md` + `UI_SLICING.md` / `COMPONENT_MAP.md`.
2. **Scan Ringkas:** Hitung metrik persentase UI Slicing dan Phase Plan.
3. **Format Output Terminal:**

```text
📊 AOD Quick Status Dashboard
──────────────────────────────────────────────────────────────────
🎨 UI Slicing Progress : [████████████░░░░░░░░] 60% (3/5 Pages Sliced)
⚡ Phase Plan Progress : [████████░░░░░░░░░░░░] 40% (Phase 2 Active)
📌 Active Git Branch   : feat/orders-checkout
🛡️ ARC Context Status  : 4 UI Refs, 2 Feature Refs in docs/references/INDEX.md
──────────────────────────────────────────────────────────────────

Quick Checklist Highlights:
[✔] Layouts Ready      : AppLayout, AuthLayout
[⏳] Current UI Slice   : OrdersListPage (Empty state WIP)
[✔] Phase 0 & Phase 1  : 100% Completed
[⏳] Active Dev Sprint  : Phase 2 — Order Checkout & Stock Lock
[ ] Blocked Items      : 0 detected

Immediate Next Steps:
1. Frontend : Tuntaskan Empty State di OrdersListPage -> jalankan "slice page OrdersListPage" (aod-page-slicer)
2. Backend  : Selesaikan inventory lock pada OrderService di branch feat/orders-checkout
3. Check Detail: Ketik "checklist ui slicing" atau "checklist phase plan" untuk rincian lengkap.
```
