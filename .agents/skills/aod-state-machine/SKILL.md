---
name: aod-state-machine
description: >-
  Defines state machine behavior for all entities with lifecycle states in
  the system. Use when the user says "state machine", "status transitions",
  "entity lifecycle", "state diagram", "mesin status", or at Phase 2 Step 8
  of AOD. Requires: Business Flow (primary) and PRD. Produces: STATE_MACHINE.md
---

# AOD: State Machine Definition Generator

## Prasyarat / Prerequisites

**Input Priority:**
1. **Business Flow (TO-BE)** *(primary — source of truth untuk states dan transitions)*
2. **PRD** *(secondary — validasi alignment dengan fitur sistem)*
3. **Study Case** *(fallback context)*

---

## Peranmu / Your Role

You are a Domain-Driven Design specialist defining state machine behavior for complex business entities.

---

## State Modeling Rules / Aturan Pemodelan State

- Setiap state harus berasal dari actual step dalam TO-BE flow.
- Setiap transition harus memiliki clear trigger.
- Sertakan failure states dan edge cases.
- Jangan menginvent states yang tidak didukung oleh flow.
- Think in domain behavior logic, NOT in UI logic.

---

## Instruksi / Instructions

**Step 1: Identify Entities Requiring State Management**
Dari Business Flow, identifikasi entitas yang memiliki states/lifecycle.

**Step 2: Define All Possible States**
List semua possible states per entitas.

**Step 3: Define Transition Table**

| From State | To State | Trigger | Actor | Conditions |
|---|---|---|---|---|

**Step 4: Define Invalid Transitions**
List transisi yang TIDAK diperbolehkan.

**Step 5: Identify Terminal States**
State yang tidak bisa ditransisi lagi (final states).

**Step 6: Define Invariant Rules**
Business rules yang harus selalu benar.

**Step 7: Identify Side Effects**
Event saat transition: notifikasi, logging, audit trail, dll.

---

## Aturan Penting / Important Rules

- Avoid ambiguous transitions.
- Do not merge states without clear justification.
- Explicitly define who is authorized to trigger each transition.
- Define invalid transitions dengan jelas.

---

## Output Format

Per entitas:
```
## Entity: [Entity Name]
### Possible States
### Transition Table
### Invalid Transitions
### Terminal States
### Invariant Rules
### Side Effects
```

---

## Output

Simpan hasil ke: `docs/system-design/STATE_MACHINE.md`
