# AOD Feedback & Revision Protocol — Always Active

## Route by intent and impact

A request to fix, add, or extend functionality in a running project uses the
scoped change workflow, not a replay of AOD phases 0–5. A new module is still a
change unless the developer explicitly requests a new-product discovery.
Read `aod-feedback-loop` and the orchestrator change-workflow reference.

- Audit/review: inspect and propose; do not edit application artifacts.
- Plan then wait: present one combined plan for document deltas, code and checks.
  Wait for the requested plan approval, then execute that entire scope.
- Apply/implement: an explicit request authorizes clear in-scope work. Summarize
  the approach and proceed; ask only about material decisions not already made.

## One authorization for the scoped change

Plan approval authorizes the described document patches, implementation,
verification and final documentation together. Do not ask for document approval,
phase mode, start confirmation or permission to run the same plan again.
Record execution authorization honestly; never claim a future document version
was personally reviewed by the developer. Pause only affected work if a new
material conflict, scope expansion or separately authorized action appears.

## Impact classes do not prescribe document volume

A: documentation-only; edit the owning sections.
B: existing behavior; use the existing contracts and patch only actual changes.
C: new capability; identify the relevant requirement/data/access/interface/UI
and architecture deltas. Do not regenerate all documents or reopen all phases.
Bug fixes restoring an existing contract need tests and implementation evidence,
not a fabricated product-specification change. A new page does not by itself
require changes to the brand, Design System or business objectives.

## Decisions before dependent code; implementation facts after checks

Before affected code, settle material business/security/architecture decisions
and patch essential contract sections listed in the authorized plan. A concise
accepted change record can supply missing focused requirements; do not generate
a complete bootstrap document set solely to allow coding. For schema, access,
interface or lifecycle changes, record the concrete contract delta before its
implementation. Follow existing project conventions and preserve their scope.
After verification, synchronize implementation details, ARC/index, applicable
UAT scenarios and actual results. Bump each changed Markdown document once per
coherent change, not for every intermediate edit. Never mark tests passed or
UAT accepted without evidence. Required documentation is part of completion.

## Reporting

Return a concise change/result/verification summary. Create a durable final
report only if the developer asks or an established project requirement needs
one; avoid duplicating a sufficient existing work item or change record.
Use the actual project Git workflow and never invent commits or approvals.
