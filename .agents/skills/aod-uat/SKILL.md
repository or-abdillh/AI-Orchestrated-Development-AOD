---
name: aod-uat
description: >-
  Creates stakeholder-ready UAT scenarios traceable to approved requirements,
  actors/roles, relevant entity states, and observable expected results. Use for
  UAT planning, user acceptance scenarios, or a UAT sheet. Requires approved
  product requirements or user-confirmed acceptance criteria; use Business
  Flow, RBAC, State Machine, and UI Flow when relevant. Produces
  docs/testing/UAT_SHEET.md.
---

# AOD User Acceptance Testing Plan

Create scenarios for stakeholders to execute and record. This skill prepares
the UAT plan; it does not execute tests, decide acceptance, or claim release
readiness. Follow `.agents/rules/aod-core.md`.

## Sources and traceability

- Use approved PRD requirements and acceptance criteria as the primary source.
- Use Business Flow for journeys/decisions; RBAC for actors and permitted or
  denied actions; State Machine for lifecycle states and transitions; UI Flow
  for screen names and navigation; BRD for business outcomes when useful.
- Use API/web-route contracts only to clarify observable behavior, not to turn
  UAT into an implementation test suite.
- If a source is absent, use only user-approved criteria available and mark
  coverage gaps. Do not invent requirements, roles, states, screens, data, or
  acceptance outcomes.

Every scenario must link to at least one stable requirement/acceptance ID. Also
identify the actor role (or `N/A` with a reason), relevant initial state and
expected final state when the requirement is stateful, and an observable
expected result. State and role must match their owning RBAC/State Machine
documents. If a requirement has no ID, propose a stable local scenario-source
reference such as PRD section number without fabricating an official ID.

## Scenario design

For each approved requirement, create a small, risk-based set of non-redundant
scenarios that covers the applicable behaviors:

- Normal successful outcome.
- Important valid alternative or boundary case.
- Validation, authorization, or failure behavior when relevant.
- Allowed and disallowed state transitions when lifecycle behavior is in scope.

Do not force every scenario type onto every feature or impose a fixed number of
cases per module. A denied-role case must name the role and expected access
outcome. A transition case must show the entity, initial state, actor/action,
precondition or guard, expected state, and user-visible/business outcome.
Separate domain states from UI states; do not turn loading/error display into
entity lifecycle states.

Write test steps in concise, business-friendly language that a stakeholder can
follow without code knowledge. Make the expected result observable and
unambiguous. Use synthetic test data or reference an approved test fixture;
never include personal or production data.

## Output: `docs/testing/UAT_SHEET.md`

Use the project document-versioning standard and
`docs/samples/UAT_SHEET_TEMPLATE.md` when present. Include:

1. **UAT Scope and Basis** — release/build under review if known, source docs,
   stakeholder audience, assumptions, exclusions, and coverage limitations.
2. **Requirement Coverage Matrix** — requirement/acceptance ID, summary,
   scenario IDs, and coverage status (`Covered`, `Partial`, `Blocked`, `N/A` +
   reason).
3. **Scenario Register** — one row per scenario with scenario ID, requirement
   ID(s), feature/module, screen or workflow, role, preconditions/initial state,
   test data, steps, expected result/final state, priority, and run fields.
4. **Role and State Coverage** — summarize relevant role/action pairs and
   lifecycle states/transitions exercised; call out gaps rather than claiming
   exhaustive coverage without evidence.
5. **Execution and Sign-off** — leave actual result, evidence, tester, date,
   status, and stakeholder decision empty or `Not Run` until stakeholders
   execute the scenarios. Include sign-off fields suited to the project.
6. **Open Decisions / Blockers** — requirements or test setup choices that
   prevent reliable acceptance.

Suggested execution statuses: `Not Run`, `Pass`, `Fail`, `Blocked`, and `N/A`
with a reason. Do not mark scenarios passed, accepted, or deployment-ready
while only generating the sheet. After saving, state the first stakeholder
execution step and any coverage limitation.
