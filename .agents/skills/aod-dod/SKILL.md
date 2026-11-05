---
name: aod-dod
description: >-
  Defines measurable, scope-specific completion criteria for AOD features,
  integrations, UI pages, and releases. Use for a Definition of Done, DoD
  checklist, or feature completion criteria. Requires the approved Tech Spec
  and Phase Plan plus applicable requirements and contracts. Produces
  docs/development/DOD.md.
---

# AOD Definition of Done

Create a practical completion gate based on the project's approved architecture,
work plan, and risk. Follow `.agents/rules/aod-core.md`. Do not impose a
framework, layer pattern, test threshold, security certification, or release
process that the project has not selected.

## Inputs and applicability

Read the approved Tech Spec and Phase Plan, then use the applicable PRD,
Business Flow, Data Dictionary, RBAC, State Machine, API Contract, UI plans,
Design System, existing code conventions, and user decisions.

- Keep universal completion criteria separate from checks that apply only to a
  database change, API/web route, UI page, integration, or deployment.
- Mark each criterion **Required**, **Conditional**, or **Not Applicable** and
  state why. Do not omit a relevant gate just because the project uses a
  different framework.
- Derive quantitative thresholds and required commands only from approved
  project documents. If none exist, define observable acceptance evidence or
  leave the threshold as an open decision.
- Distinguish expected checks from evidence that checks have actually run.
  Never mark a check passed without a recorded result.

## Criteria to define

Build a feature/release checklist from these areas, including only relevant
criteria:

1. **Scope and behavior** — approved work item, user-visible outcomes,
   acceptance criteria, exclusions, and failure/edge behavior.
2. **Domain and data integrity** — source-backed fields, validation,
   constraints, transactions/concurrency where required, and State Machine
   invariants.
3. **Authorization and security** — RBAC rules at the actual enforcement point,
   data exposure, input handling, and applicable privacy/security requirements.
4. **Architecture and integration** — Tech Spec boundaries, API or web-route
   contract, error behavior, external dependencies, and compatibility.
5. **UI quality** — only for UI scope: approved design tokens, relevant visual
   states, responsive/accessibility behavior, and UI acceptance evidence.
6. **Verification** — checks and test cases required by the project plan, with
   exact expected evidence; include manual/UAT checks only when applicable.
7. **Operations and documentation** — migration/release/monitoring needs when
   applicable, and ARC/reference updates required by the project's DoD.

For ARC, distinguish an implemented UI page reference (`REF-UI-*`, Phase 4)
from an implemented backend/integration feature reference (`REF-FEAT-*`, Phase
4). Require `docs/references/INDEX.md` updates when the project's documentation
policy requires them. Record actual files, contracts, invariants, integration
handoff, and verification evidence; do not require an ARC reference for a
documentation-only task unless the project explicitly requires one.

## Checklist semantics

Each criterion must have a stable ID, applicability, observable evidence, and
one status: `Pass`, `Fail`, `Blocked`, `Not Run`, or `N/A` with rationale.
Completion requires every Required criterion to pass and every Conditional
criterion to be resolved. A failed, blocked, or unrun required check is not
complete. Keep acceptance status distinct from release/deployment approval.

## Output

Save to `docs/development/DOD.md` using the project's document versioning
standard. Include scope, source documents, checklist semantics, core criteria,
conditional criteria by work type, evidence fields, and unresolved thresholds
or decisions. If a Phase Plan exists, map criteria to its work item or exit
criteria. After saving, identify `aod-uat` as the next step when UAT is in
scope; otherwise state the next dependency-ready action.


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
