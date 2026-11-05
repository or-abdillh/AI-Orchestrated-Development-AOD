# Checkpoint contract — schema 1

Use Python 3 standard library, no package installation. Helpers do not execute
skills and cannot independently verify the authenticity of developer approval.
`workflow.baseline(registry, project, scope, checkpoint_path)` creates an in-memory
candidate only after start confirmation. Store schema_version, registry_version,
workflow_id/scope, project/checkpoint paths, active phase/step, mode, authorization,
steps, source SHA-256 values, artifact versions/paths, decisions and scoped
approvals, blockers, pending_decisions, next_action, failures, pause flag,
revision and updated_at. Approvals record actor, explicit response, time, scope,
and source version/fingerprint; keep sensitive values out.

Every unit stores status, artifacts, sources (project-relative consumed file to
SHA-256), evidence, approved boolean and reason. Record actual consumed sources
and test/code evidence, not just registry-level dependencies. Store baseline
facts separately from approval. Reconstructed existing documents may have review
pending; preserve valid work and ask only ambiguous decisions. Never infer
approval from filename, commit, or document existence.

Transitions enforced by `TRANSITIONS` in workflow.py:
Pending → Ready/Blocked/Skipped; Ready → In Progress/Blocked/Skipped;
In Progress → Awaiting Review/Completed/Blocked/Failed;
Awaiting Review → Completed/In Progress/Blocked/Needs Revalidation;
Completed/Skipped → Needs Revalidation; Blocked/Failed → retry readiness;
Needs Revalidation → Ready/Awaiting Review/Blocked/Completed/Skipped.
Completion requires exit evidence and required explicit approval. Skipping
requires a reason. In Progress after interruption must be examined, never
silently completed. Preserve partial artifacts and failures with recovery action.

Run `python3 .agents/skills/aod-orchestrator/scripts/workflow.py validate-registry`.
Use `inspect --state <path>` for read-only readiness/revalidation/phase-exit
checks. It reports reconciled state without writing. Reconcile and invalidate
in-memory state before any save or resume, and refresh fingerprints only after
reviewing changes. Clear impacted approval; do not invalidate unrelated branches.

Write a proposed JSON to a temporary path and use `save --state <path>
--candidate <temporary-json> --expected-revision <loaded-revision>`; initial
revision expectation is -1. Save validates before atomic replacement, uses a
same-directory temporary file with fsync, and an exclusive lock plus revision
comparison to reject competing writes. Main agent is the sole writer. On stale
lock, inspect recorded PID/time and active agents before explicitly removing it;
never steal a live lock. On malformed state, unsupported schema or registry
version, preserve the original bytes, report the issue, and recover/migrate to
a separate validated copy after developer resolves any lost approval evidence.
Do not overwrite original until recovery is explicitly accepted.

JSON state uses schema/revision metadata rather than Markdown document headers.


Existing selected as-is documents may record `baseline_overrides` entries:
`{step_id, scope: "as-is", depends_on: [], evidence: [path/reference],
authorization: "explicit selected as-is scope response"}`. Use only when existing
initiation evidence replaces bootstrap inputs; the artifact itself still needs
its required review. Never override target implementation, adapter, plan,
prompts or DoD gates. Pass `effective_registry(state, registry)` to validation,
readiness, invalidation and phase closure. Dynamic and override graph errors
reject state; unknown target decisions remain blocked.

## Additive change profile

Absent profile means guided; schema 1 guided checkpoints remain compatible and
are never converted in place. Use change_baseline/init-change and a separate
change file as described in change-workflow.md. Change review_required=false
units require evidence under a fingerprint-bound execution plan, not invented
manual approval. Change source reconciliation preserves review history and
marks only changed consumers until a documented impact assessment determines
the affected descendants. The old broad invalidation remains for guided
checkpoints; do not use that scheduler for incremental work.
