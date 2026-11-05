# Specialist handoff

When orchestrated, return this record to the main agent (in chat or tool result,
not a new product file unless required). A direct invocation returns the same
facts to the developer and stops within its requested scope.

- Step ID and skill; source snapshot paths and fingerprints.
- Created/updated artifact paths, versions, and summary.
- Draft, awaiting review, or explicitly approved status and approval scope.
- Exit-criteria evidence, actual verification commands and results.
- Open decisions, blockers, failures and partial outputs.
- Dependencies newly ready and recommended next step.

The orchestrator checks the handoff against actual files; claims alone never
prove completion or approval. It alone updates workflow state. A specialist's
legacy “next skill” message is a recommendation, not a request that the developer
invoke it manually or authorization to continue.

## Scoped change handoff

When the change profile is active, patch only requested owning sections. Check
relevant existing contracts; a missing bootstrap document does not require a
full generation chain. Use the accepted delta plan as scope authority. Return
validation evidence and execution-plan provenance; do not label a plan-derived
document as personally reviewed by the developer. Do not ask for a new approval
for faithful execution or route through phases. Material new decisions remain
open. The main agent continues within the existing authorization.
