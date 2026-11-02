---
name: aod-ui-flow
description: >-
  Defines application screens, role-based journeys, navigation, interaction
  rules, and screen-to-API traceability. Use when the user asks for a UI flow,
  screen map, user journey, application screens, or the AOD system-design UI
  flow. Requires approved product requirements as the primary source and uses
  Business Flow, RBAC, State Machine, and API Contract when available.
---

# AOD UI Flow and Screen Map

Define what users can see and do, and how screens connect. This document is an
interaction contract; it does not choose visual styling, component hierarchy,
or implementation architecture. Follow `.agents/rules/aod-core.md` and
preserve the authority of approved upstream documents.

## Inputs and Evidence

Use the following sources as applicable:

- **Approved PRD:** feature scope, actors, user goals, and acceptance intent.
- **Business Flow:** operational sequence and system or human actions.
- **RBAC:** roles and permission conditions.
- **State Machine:** entity states and allowed transitions.
- **API Contract:** available interface operations and payload references.

Record the source section or requirement ID for each material screen, action,
visibility rule, and state-dependent behavior. If a required decision is absent,
mark it open; do not invent screens, roles, endpoint paths, or state transitions.
Draft the supported portions and identify what remains blocked.

## Modeling Rules

- Include only screens supported by a product requirement, business workflow,
  or explicit user decision. Mark optional or proposed screens as such.
- Give each screen a stable ID, name, route when defined, purpose, allowed
  actors/roles, entry conditions, and primary user goal.
- Describe journeys as ordered steps: actor, action, system response, resulting
  screen or state, and relevant failure or alternate path.
- Define visibility and enabled/disabled behavior from RBAC and State Machine
  rules. Reference their source instead of restating or changing those rules.
- Map an action to an API operation only when it exists in the approved API
  Contract. If the interaction needs an undefined operation, record an API gap
  for the owner to resolve.
- Include loading, empty, error, success, and permission-denied behavior when
  supported by the screen's data or action. Do not use a visual color or style
  as a state definition.
- Note friction, destructive actions, confirmation needs, and accessibility
  implications where they affect interaction.

## Output: `docs/system-design/UI_FLOW.md`

Use the project's document versioning standard. Include:

1. **Scope and Sources** — document status, source documents, assumptions, and
   open decisions.
2. **Screen Index** — stable screen ID, name, route if defined, roles, purpose,
   and source requirement IDs.
3. **Role Journeys** — journey ID, starting condition, ordered steps, alternate
   paths, failure cases, and outcome.
4. **Screen Interaction Contract** — for each screen:
   - Entry conditions and permitted actors.
   - Primary and secondary actions.
   - Visibility/enabled conditions with RBAC or State Machine references.
   - Data needs and API Contract references, or an explicit unresolved gap.
   - Loading, empty, error, success, and denied states as relevant.
5. **Cross-Screen Navigation** — transitions between screen IDs and their
   triggers.
6. **Open UX and Contract Decisions** — missing requirement, role, state, route,
   or API decision; owner and affected screens.

Do not specify component trees here; `aod-ui-component-map` derives those from
this screen contract. After saving, identify the next valid step, usually
`aod-ui-component-map` when the relevant design inputs are available.


## Orchestrator handoff

When invoked by `aod-orchestrator`, read
`.agents/skills/aod-orchestrator/references/handoff.md`, return its structured
handoff, and return control to the orchestrator. Do not write workflow checkpoint.
Direct invocation authorizes only the requested scope, not the full workflow.
