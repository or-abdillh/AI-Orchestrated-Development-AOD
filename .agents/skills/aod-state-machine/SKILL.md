---
name: aod-state-machine
description: >-
  Defines approved domain lifecycle states, transitions, guards, actors, and
  invariants for entities that change status. Use for a state machine, status
  transition map, or entity lifecycle. Requires Business Flow (TO-BE) and PRD;
  use Data Dictionary and RBAC when available. Produces
  docs/system-design/STATE_MACHINE.md.
---

# AOD State Machine

Model domain lifecycle behavior from approved business sources. Follow
`.agents/rules/aod-core.md`. Keep domain lifecycle separate from presentation
states such as loading, empty, and error.

## Sources and boundaries

- Use Business Flow (TO-BE) for actual operational steps and triggers; PRD
  confirms feature scope and intended outcomes.
- Use Data Dictionary for entity identity and persisted status fields, and RBAC
  for actor authorization when available.
- For existing systems, distinguish observed states/transitions from proposed
  behavior and cite implementation evidence separately.
- Do not infer a state merely because it is common in similar systems. Record
  ambiguity, missing trigger, or conflicting sources as an open decision.

## Model each lifecycle

For every entity with meaningful lifecycle behavior, document:

1. Entity and lifecycle scope, with source references.
2. States, definitions, entry conditions, and whether terminal or re-enterable.
3. Allowed transitions in a table:

   | From | To  | Trigger/event | Actor | Guards/preconditions | Result/side effects | Source |
   | ---- | --- | ------------- | ----- | -------------------- | ------------------- | ------ |

4. Invalid or explicitly forbidden transitions, including why when known.
5. Invariants that must hold before and after transitions.
6. Failure, cancellation, retry, timeout, or reversal paths only when supported
   by the business sources.
7. Authorization dependencies and related data fields, linked to RBAC and the
   Data Dictionary rather than redefining them.

Use precise transition names and distinguish a business event from the actor
action that causes it. State whether a transition is reversible only when the
source defines that behavior. Do not treat HTTP response statuses or visual UI
states as entity lifecycle states.

## Output

Save to `docs/system-design/STATE_MACHINE.md` using the project's document
versioning standard. Organize by entity and include source traceability, allowed
and forbidden transitions, invariants, side effects, and open decisions. If no
entity has an evidenced lifecycle, state that finding instead of manufacturing
a state machine. Identify downstream API/UI contracts that depend on approved
transitions.


## Orchestrator handoff

When invoked by `aod-orchestrator`, read
`.agents/skills/aod-orchestrator/references/handoff.md`, return its structured
handoff, and return control to the orchestrator. Do not write workflow checkpoint.
Direct invocation authorizes only the requested scope, not the full workflow.
