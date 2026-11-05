---
name: aod-design-system
description: >-
  Defines framework-neutral visual principles, component behavior, layout,
  accessibility, and consistency rules from an approved Website Concept. Use
  for a design system, UI guidelines, or component standards. Requires the
  Website Concept for new products; for existing products use verified UI
  evidence and label missing design decisions. Produces
  docs/system-design/DESIGN_SYSTEM.md.
---

# AOD Design System

Define the product's visual and interaction system in terms that can be
implemented by the project's selected technology. Follow `.agents/rules/aod-core.md`.
This document is the design authority; it does not choose a CSS framework or
write implementation configuration.

## Sources and boundaries

- Use Website Concept for product personality, users, content, and UX direction.
- Use approved product requirements and UI Flow for the needs and interactions
  the system must support.
- For an existing product, inspect current visual conventions and distinguish
  observed patterns from approved target changes.
- Do not adopt a reference style wholesale or create a component without a
  demonstrated product need. Mark unresolved visual decisions rather than
  treating recommendations as approved.
- Keep this document framework-neutral. Concrete token values belong in
  `UI_STYLE.md`; framework-specific token mapping belongs in
  `aod-tailwind-config` after the stack is approved.

## Define the system

1. **Principles and visual identity** — a small set of decision rules grounded
   in the product concept; avoid generic adjectives without design implications.
2. **Color roles** — semantic roles and usage (surface, text, action, status,
   focus, border); leave concrete color values to UI Style.
3. **Typography roles** — hierarchy and content use, not framework class names.
4. **Spacing, layout, and responsive behavior** — principles and content
   relationships; avoid arbitrary fixed dimensions unsupported by the product.
5. **Component inventory** — only components justified by product workflows;
   define purpose, composition, variants, and behavior at the design level.
6. **Interaction and states** — default, hover where applicable, active,
   focus-visible, disabled, loading, empty, error, and domain states as relevant.
7. **Data/status presentation** — rules for tables, charts, filters, summaries,
   and semantic statuses grounded in requirements.
8. **Accessibility** — contrast intent, keyboard behavior, focus visibility,
   semantics, readable content, and non-color status cues.
9. **Motion and feedback** — when to animate, timing intent, reduced-motion
   behavior, and feedback patterns where relevant.
10. **Anti-patterns** — concrete examples of inconsistency to avoid, without
    banning valid patterns the product may require.

## Output

Save to `docs/system-design/DESIGN_SYSTEM.md` using the project document
versioning standard. Include source references, approved principles, component
behavior, accessibility, and open decisions. Do not put Tailwind classes,
framework config, or arbitrary token values in this document. After saving,
identify `aod-ui-style` as the next step for the canonical token values.


## Scoped changes

For an initialized product change, read
`.agents/skills/aod-orchestrator/references/change-workflow.md`
and follow its minimum section-level delta and single-authorization contract.
The existing approved baseline and accepted change plan supply relevant inputs;
do not require full bootstrap generation or duplicate document approvals.
Preserve material unresolved decisions. This does not broaden audit-only scope.

## Orchestrator handoff

When invoked by `aod-orchestrator`, read
`.agents/skills/aod-orchestrator/references/handoff.md`, return its structured
handoff, and return control to the orchestrator. Do not write workflow checkpoint.
Direct invocation authorizes only the requested scope, not the full workflow.
