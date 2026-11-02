# Operating protocol

## Inspect and authorize

Read agent instructions, Git status, available AOD documents, approvals and
checkpoint. Do not run project scripts or write documents during screening.
Classify new project, existing adoption, or active AOD. For existing adoption,
read `aod-existing-project-initiation` and perform its read-only screening.
Its evidence-based as-is exception may replace bootstrap dependencies only for
selected as-is documents; never use that exception to approve target decisions.

Present goal/scope, relevant phases, step IDs and skills, outputs, missing
inputs/decisions, completed or skipped work with evidence/reasons, and candidate
parallel waves. Then ask: **Mulai dengan rencana ini / Sesuaikan rencana /
Belum mulai**. Do not create checkpoint or product artifacts before explicit
start approval. This is the product workflow gate, not a gate to editing the
skill pack itself. Existing explicit approval for the same scope is reusable.

Discover actual platform question capabilities; never invent a tool call or
require a named tool. If unusable, show numbered choices in chat and wait for
explicit answers to mandatory gates. Timeout, empty response and no response
never authorize work. Label optional preferences separately from required gates.

## Phase authorization and scheduling

Before each relevant phase show its work and request a mode:

1. **Bertahap (step):** one ready unit, summary, checkpoint, then wait for lanjut.
2. **Satu fase dengan sub-agent (phase-parallel):** independent units in dependency
   waves; no downstream task before its actual required sources are ready.
3. **Satu fase berurutan (phase-sequential):** ready units sequentially.

Record phase, mode, scope, approving developer response and source-plan
fingerprint. Start approval and phase mode may be answered together, but both
must be explicit. Phase execution is not document approval, architecture
approval, deployment, publication, or permission to contact external services.
Material unresolved decisions stop affected work; continue independent work
only within authorization. In step mode any completed or blocked attempted unit
ends the execution allowance until the developer continues.

Select applicability explicitly. Mark irrelevant/optional units Skipped with a
reason; never skip a required prerequisite to make downstream work ready.
Tie-break ready units by registry order, respecting developer priorities.
Read the chosen specialist, confirm its actual prerequisites, execute it, then
inspect output and reconcile evidence. Drafts requiring review become Awaiting
Review, not Completed. Review may cover multiple artifacts only if scope and
versions are explicit. Route-neutral contracts may precede Tech Spec; after
Tech Spec approval revalidate only affected contracts. Never assume Sanctum,
Tailwind, or a framework. Styling adapter is planned Phase 4 implementation.

## Parallel waves

Delegate only if actual platform capability exists and phase-parallel is
selected. Each assignment specifies ID, exclusive file ownership, outputs,
source paths and hashes, acceptance criteria and scope. Agents must not write
checkpoint or shared ARC index. Main agent integrates shared updates after
review. Avoid conflicting outputs and decisions even if graph dependencies
permit concurrency. Recheck source hashes on return; changed sources require
revalidation before integration. If a delegate fails, record Failed and partial
outputs. Report fallback; use sequential execution only when developer permits
it, otherwise request the fallback choice. Never claim parallel execution based
on a planned wave.

## Dynamic development and phase closure

Expand approved Phase Plan item IDs as `impl:<item-id>` with explicit dependency
IDs, relevant approved contracts, output owners, evidence and exit criteria.
Record these definitions in checkpoint `dynamic_steps`; validate their graph
with the static registry. Add `aod-page-slicer` for mock UI units; backend and
integration units use their approved feature prompt and coding workflow.
Shared ARC index is integrated by the main agent. DoD, actual checks and ARC
are required before implementation completion. Product releases/sprints remain
metadata and never replace AOD methodology phase IDs.

Before phase closure check selected units and exit criteria, current source
versions, approvals and blockers. Report Completed, Skipped, Blocked, Failed,
and Needs Revalidation. Ask explicit confirmation and mode for the next phase;
never advance automatically under the previous phase's authorization.
Separate workflow steps, requirement implementation, verification results,
and UAT preparation/execution/acceptance. A UAT sheet is not executed UAT.
If reporting percentages, state selected unit denominator and exclusions; never
label step counts as product completion.

Feedback follows `aod-feedback-loop`: update owning upstream sources before
implementation and invalidate affected dependents. Quick Checklist remains
read-only and concise; Progress Tracker independently audits evidence and only
exports when asked. Neither writes checkpoint success.


## Resume details

An explicit lanjut replenishes one step allowance: call `continue_step(state)`
or set authorization.unit_consumed=false after recording that response. Do not
clear pending decisions or approve artifacts. Pending material decisions use
`{id, question, blocks: [step-id, ...]}`; list affected transitive unit IDs so
independent work remains eligible. Unknown/unscoped legacy decisions block all
execution until their impact is understood.

The registry `implementation` row is an aggregation placeholder, never an
executable unit. Once approved Phase Plan items are expanded, mark it Skipped
with reason pointing to dynamic IDs. Phase closure uses effective_registry,
including every dynamic child. It cannot close while a child is unfinished.
