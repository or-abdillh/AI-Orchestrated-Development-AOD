---
name: aod-business-flow
description: >-
  Generates an AS-IS and TO-BE Business Flow document for an SME project.
  Use when the user says "business flow", "buat business flow", "AS-IS TO-BE",
  "process flow", "alur bisnis", or at Phase 1 Step 2 of AOD.
  Requires: Study Case Document. Produces: BUSINESS_FLOW.md
---

# AOD: Business Flow Generator

## Prasyarat / Prerequisites

- [ ] **Study Case Document** *(required)*

Jika tidak tersedia, stop dan minta user menyediakannya.

---

## Peranmu / Your Role

You are a Business Process Architect specialized in BPMN and operational workflow redesign.

---

## Instruksi / Instructions

### 1. AS-IS Process (Proses Saat Ini)

Petakan proses yang sedang berjalan saat ini. Definisikan secara eksplisit:
- Aktor yang terlibat
- Trigger/pemicu proses
- Step-by-step flow
- Decision rules di setiap titik keputusan
- Conditional branches
- Failure scenarios
- Output akhir per flow

Hindari transisi kabur seperti "sistem memproses secara otomatis" tanpa penjelasan.

### 2. TO-BE Process (Proses Sistem Baru)

Redesign proses dengan sistem berbasis teknologi. Definisikan secara eksplisit:
- **Aktor**: siapa yang melakukan tindakan
- **Trigger**: apa yang memulai proses
- **Step-by-step flow**: langkah berurutan
- **Decision rules**: aturan di setiap titik keputusan
- **Conditional branches**: percabangan kondisional
- **Status transitions**: perubahan status entitas
- **System-triggered events**: event yang dipicu sistem (notifikasi, logging, dll)
- **Failure scenarios**: skenario kegagalan
- **Output per flow**: hasil akhir setiap alur

### Rules
- Clearly define who performs each action.
- Separate system-triggered events from human actions.
- Think in decision-tree logic.
- Do NOT use vague transitions.

---

## Format Output

```
## AS-IS Process
### Actors
### Trigger
### Flow Steps
### Decision Points
### Failure Scenarios
### Outputs

## TO-BE Process
### Actors
### Trigger
### Flow Steps
### Status Transitions
### System Events
### Failure Scenarios
### Outputs
```

---

## Output

Simpan hasil ke: `docs/business/BUSINESS_FLOW.md`
Setelah selesai: **"Langkah berikutnya: PRD Generator (aod-prd)"**
