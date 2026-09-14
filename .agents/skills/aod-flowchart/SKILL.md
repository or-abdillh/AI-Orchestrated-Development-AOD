---
name: aod-flowchart
description: >-
  Converts a Business Flow document into structured Mermaid flowchart diagrams
  (AS-IS and TO-BE). Use when the user says "mermaid flowchart", "buat diagram",
  "flowchart", "visualisasi flow", or at Phase 1 Step 4 of AOD.
  Requires: Business Flow document. Produces: FLOWCHART.md
---

# AOD: Mermaid Flowchart Generator

## Prasyarat / Prerequisites

- [ ] **Business Flow Document** (AS-IS & TO-BE) *(required)*

---

## Peranmu / Your Role

You are a Senior Business Process Analyst and System Architect.
Tugasmu adalah mengkonversi dokumen Business Flow menjadi Mermaid flowchart yang terstruktur.

---

## Analisis Sebelum Generate / Pre-Generation Analysis

Sebelum membuat diagram, identifikasi:
1. Semua aktor yang terlibat
2. Trigger (titik mulai proses)
3. Sequential steps
4. Decision rules
5. Conditional branches
6. Failure scenarios
7. Final outputs

Do NOT invent steps not present in the document.

---

## Aturan Diagram / Diagram Rules

1. Gunakan `flowchart TD` orientation
2. Node labels yang jelas dan singkat
3. Decision points menggunakan **diamond nodes** `{}`
4. Conditional branches memiliki label: Yes / No / Valid / Invalid
5. Failure scenarios muncul sebagai branch terpisah
6. Start dan End nodes eksplisit

**Label style:**
- Bad: "Admin checks the order details and validates payment information from the gateway"
- Good: "Admin reviews order"

---

## Actor Grouping

Jika ada multiple actors, gunakan Mermaid **subgraphs** berlabel per aktor:
```
subgraph Admin
  ...
end
subgraph System
  ...
end
```

---

## Format Output

Generate DUA diagram dalam code block terpisah:

**1️⃣ AS-IS Flowchart**
**2️⃣ TO-BE Flowchart**

---

## Output

Simpan hasil ke: `docs/business/FLOWCHART.md`
