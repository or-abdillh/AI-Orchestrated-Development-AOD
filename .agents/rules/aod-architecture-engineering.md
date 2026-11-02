---
trigger: always_on
---

# AOD Dynamic Architecture Rule — Project-Specific Policy Gate

> **Purpose:** Resolve and apply the approved project architecture rules. This
> file is a policy gate, not a substitute for the project's Technical
> Specification.
> **Authority:** `docs/development/TECH_SPEC.md` and approved decisions referenced there.
> **Generated project rules:** Replace this template with concise rules derived
> from approved project constraints when `aod-tech-spec` is authorized to do so.

## Governing Instructions

- Before implementing or refactoring a feature, read the relevant sections of
  `docs/development/TECH_SPEC.md`, this file, and any approved architecture
  mirror at `docs/development/ARCHITECTURE_ENGINEERING.md`.
- Apply only project-specific constraints that are explicitly marked
  **Approved** in the current Technical Specification. A recommendation,
  assumption, example, or open decision is not an active constraint.
- Use the named frameworks, libraries, versions, directory boundaries, and
  conventions verified or approved for this project. Do not infer project
  architecture from this file's examples or from another framework's defaults.
- If this file conflicts with the current approved Technical Specification,
  stop only the affected implementation, report the conflicting statements and
  sources, and request resolution. Do not silently choose one or expand scope.
- If the Technical Specification is missing, Draft, or does not define a needed
  decision, follow existing project conventions where they are evidenced and
  safe; otherwise mark the choice open and ask only when it blocks the task.
- Follow the authority of upstream project documents for business requirements,
  data schema, API contracts, permissions, lifecycle states, and design tokens.
  Do not redefine these in an architecture rule.
- Keep this file short, actionable, and limited to constraints that must remain
  available across implementation sessions. Store rationale and detailed
  alternatives in the Technical Specification.

## Activation and Replacement

- This gate may remain `always_on` because it defines how to resolve project
  architecture policy; it does not itself approve a proposed project design.
- `aod-tech-spec` may replace this gate with project-specific `always_on` rules
  only after the relevant Tech Spec constraints are approved and the user has
  selected or requested that rulebook output.
- Preserve unrelated local rules. When updating project-specific rules, update
  this file and its documentation mirror together, with version and revision
  history in the mirror.
