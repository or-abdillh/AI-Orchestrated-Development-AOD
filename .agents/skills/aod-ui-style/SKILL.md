---
name: aod-ui-style
description: >-
  Converts approved product direction and Design System rules into a canonical,
  framework-neutral visual token and styling specification. Use for UI Style,
  style guide, or design token definition. Requires Website Concept and Design
  System for new products; for existing products use verified UI evidence and
  label missing design decisions. Produces docs/system-design/UI_STYLE.md.
---

# AOD UI Style Specification

Define concrete design decisions that designers and implementation agents can
apply consistently, without coupling the canonical style source to a CSS
framework. Follow `.agents/rules/aod-core.md` and treat the Design System as the
authority for component and interaction rules.

## Sources and boundaries

- Use Website Concept for product tone and visual direction, Design System for
  roles, components, states, and accessibility, and UI Flow for actual screens
  and content needs.
- For an existing project, inspect its current styles and tokens. Separate
  observed values from approved target values and avoid needless token churn.
- Define semantic token names and values here; do not use Tailwind classes,
  framework configuration syntax, or prescribe component implementation
  patterns.
- Do not invent a visual direction or resolve open product decisions by taste.
  Label recommendations and unresolved tokens.

## Define canonical tokens

Use a stable semantic naming scheme. For each token record its name, value,
purpose, usage, and relevant contrast/accessibility constraints. Include the
systems required by the Design System:

- **Color:** semantic roles for text, surfaces, borders, actions, focus, and
  statuses; provide exact values and contrast pairings where applicable.
- **Typography:** font families/fallbacks, roles, sizes, weights, line heights,
  and tracking, using explicit units.
- **Spacing and layout:** a reusable scale, container/content widths, grid and
  breakpoint intent; distinguish design intent from framework breakpoint
  syntax.
- **Shape and elevation:** radii, borders, shadows/elevation, and when each is
  used.
- **Motion:** duration/easing roles, transition intent, and reduced-motion
  behavior when motion is used.
- **Component styling:** map component variants and states to semantic tokens
  from the Design System; include only components the product needs.

Keep raw values and semantic aliases traceable. Ensure statuses remain
distinguishable beyond color alone. Do not define duplicate tokens for the same
meaning; provide a deprecation/migration note when replacing existing tokens.

## Output: `docs/system-design/UI_STYLE.md`

Use the project's document versioning standard. Include source documents,
visual direction, canonical token tables, component/state mapping, contrast and
accessibility notes, responsive/motion rules, anti-patterns, and open decisions.
Add a short implementation note: `aod-tailwind-config` maps these canonical
tokens to the project's approved styling system; that mapping must not redefine
the token source. After saving, identify `aod-ui-slicing` as the next step when
its inputs are ready.
