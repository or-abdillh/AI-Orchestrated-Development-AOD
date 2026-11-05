# Scoped change workflow

## Routing and authority

Use this profile for bug fixes, feature changes and new modules in an existing
product. Reuse the baseline and approved decisions; no Phase 1–5 replay, global
screening or bootstrap document generation. Guided discovery remains available
for new products or an explicit developer preference. A specialist invocation
alone authorizes only its requested task.

The developer authorizes a change scope, not an administrative phase transition.
For plan-and-wait, present one combined plan then wait once. For an explicit
apply request, reuse that directive as authorization for clear work. Never ask
again for the same scope. Material questions still require actual answers;
silence, empty widgets and timeout never approve a decision.

## Combined plan

State scope, acceptance criteria, existing constraints, exact document paths and
sections with impact reasons, implementation work, verification, exclusions and
unresolved material decisions. Separate essential before-code contract changes
from after-verification factual documentation. An empty document delta list is
valid for a bug that restores the existing specification. Do not invent rates,
architecture, permissions, route/auth styles, or product decisions.

Use the existing work item/plan when adequate; a separate plan file is optional.
Feature Prompt Library and full Phase Plan regeneration are not mandatory
intermediaries for a focused change with a concrete authorized implementation
plan. Existing relevant DoD and ARC requirements still apply.

## Execute to completion

Default is change-sequential, covering contracts → implementation → verification
→ factual documentation. These are work stages, not methodology phases, and
need no repeated start/mode/document approvals. A contracts stage with no delta
records that the existing specification was checked, then continues immediately.
Only substantial changed decisions need developer review. Check document patches
against the authorized plan; do not fabricate human document sign-off.

Use sub-agents only when authorized/capable and outputs are independent. Reuse
session parallelism preferences; no question before each stage. The main agent
owns checkpoint and shared index writes. No deployment/publication permission
is inferred. Step mode remains an explicit developer option; a summary is not
an instruction to wait in execute-to-completion mode.

Specialists patch only owning sections, preserve IDs and unrelated content,
return concrete deltas and evidence, and stop prescribing bootstrap successor
skills. Missing documents trigger a minimum focused record, not compulsory full
generators. Material missing decisions block only affected work. Follow the
approved stack and existing API/web/mixed choice; do not re-ask unchanged choices.

## Checkpoint helpers

Preserve `docs/aod/WORKFLOW_STATE.json` and its historical discovery approvals.
Use `docs/aod/changes/<id>.json` for an independent scoped change when continuity
is needed. Small direct tasks may report status in the existing work item rather
than creating another checkpoint. Never initialize a new change on top of an
existing state file. All state is written by the main agent only.

A plan JSON contains id, scope, document_changes (path, section, reason, timing:
before-code or after-verification), implementation (nonempty descriptions),
verification (nonempty descriptions). Keep acceptance criteria and exclusions in
scope or additional plan fields. Store no secrets.

After actual authorization:
`python3 .agents/skills/aod-orchestrator/scripts/workflow.py init-change --project . --state docs/aod/changes/<id>.json --plan <plan.json> --response <actual-developer-directive>`

The helper creates four dependent units and binds authorization to the plan's
fingerprint. Editing the plan does not silently retain permission. A changed
scope requires reconciliation with the developer's existing or new directive;
preserve authorization history. Helpers cannot authenticate an approval: the
agent must record the actual directive, never invent one to satisfy validation.
Use existing inspect/save helpers and revision checks for resume. A material
question uses pending_decisions with affected step IDs; add decision_dependencies
where a particular explicit decision is required. Reuse documented decisions.

Change units have review_required=false: evidence-backed completion is agent
verification under an authorized plan. The approved boolean remains reserved
for actual explicit review; no change pipeline unit needs fabricated approval.
Guided checkpoints retain their existing review behavior and schema 1 compatibility.

## Source changes

Hashes detect differences, not business impact. Change-profile inspection marks
only consumers with changed sources for assessment and preserves prior approval
history. It does not immediately invalidate every downstream unit. Read the diff:
- Editorial/metadata only: call resolve_source_change with classification
  editorial and concrete assessment evidence; update reviewed fingerprints and
  restore the consumer's prior status. Missing files are never editorial.
- Contract/behavior change: call with classification contract and evidence;
  impacted descendants require revalidation. If outside the accepted plan,
  resolve the scope first. Revalidate affected work, not a full phase replay.

Do not refresh a hash merely to bypass a changed decision. Engine helpers do not
automatically understand document semantics; impact assessment requires review.

## Exit and efficiency

Completion requires approved scope implemented, relevant verification results,
required docs/ARC synchronized, and no unresolved blockers. UAT scenarios are
not stakeholder acceptance. Report actual changes, checks, limitations and
remaining work. Log time-to-first-code, human approval count, redundant approval
count and document changes in chat/work item when available; do not invent times.
Target one approval for plan-and-wait with no new material decisions, and no
additional approval for a clear already-authorized apply request. There is no
fixed speed guarantee; test on real projects before claiming agent efficiency.
