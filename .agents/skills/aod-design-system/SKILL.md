---
name: aod-design-system
description: >-
  Generates a complete Design System Document defining visual identity, color
  system, typography, spacing, layout, component library, and accessibility
  guidelines. Use when the user says "design system", "sistem desain",
  "UI guidelines", "panduan UI", or at Phase 2 Step 12 of AOD.
  Requires: Website Concept Document. Produces: DESIGN_SYSTEM.md
---

# AOD: Design System Document Generator

## Prasyarat / Prerequisites

- [ ] **Website Concept Document** *(required)*

---

## Peranmu / Your Role

You are a Senior Design System Architect and Product UI Designer.

---

## Design Philosophy

Prioritaskan: Consistency, Clarity, Scalability, Usability, Maintainability.

---

## Struktur Dokumen / Document Structure

**1. Design Principles** — Prinsip panduan berdasarkan product vision
**2. Visual Identity** — modern, minimal, professional, data-focused
**3. Color System** — Primary, Secondary, Neutral, Success, Warning, Danger, Info (hex + usage)
**4. Typography System** — Display, Heading, Subheading, Body, Caption, Label (+ guidance)
**5. Spacing System** — 4px/8px/12px/16px/24px/32px/48px/64px + usage rules
**6. Layout System** — Container width, grid, sidebar, responsive behavior
**7. Component Library:**
- Navigation: Sidebar, Navbar, Breadcrumb
- Forms: Input, Select, Checkbox, Radio, Textarea, Date Picker
- Data Display: Table, Card, List, Statistic Block
- Feedback: Alert, Toast, Modal, Confirmation Dialog
- Status: Badge, Tag, Progress Indicator
- Actions: Button, Dropdown, Menu, Pagination
**8. Interaction States** — default, hover, focus, active, disabled, loading
**9. Status Visualization** — success, pending, processing, warning, error
**10. Data Presentation Guidelines** — tables, dashboards, filters, summaries
**11. Accessibility Considerations** — contrast (WCAG AA min), keyboard, focus indicators

---

## Output Requirements

- Avoid referencing specific CSS frameworks — focus on universal principles.
- Be suitable for AI agents to follow when generating UI.

---

## Output

Simpan hasil ke: `docs/system-design/DESIGN_SYSTEM.md`
