---
name: aod-orchestrator
description: >-
  Run AOD through one entry point: Mulai AOD, Lanjut AOD or lanjut, Status AOD,
  Jeda AOD, and Ubah mode AOD. Inspect new, existing, or active projects, obtain
  scoped start and phase authorization, execute dependency-ready specialist
  skills, and preserve resumable checkpoints. Direct specialist requests remain
  scoped and do not authorize the entire workflow.
---

# AOD Orchestrator

Read `.agents/rules/aod-core.md` and [the operating protocol](references/protocol.md).
Use [workflow.json](references/workflow.json) as the workflow registry, not a
memorized skill sequence. Read the selected specialist's actual `SKILL.md`,
execute its instructions when ready, inspect its output, and return control here.
Never tell the developer to manually invoke the next specialist.

## Commands

- **Mulai AOD:** inspect read-only, classify new/existing/active, present the
  overview, then obtain explicit start confirmation. Reuse explicit approval
  for the same plan in the active conversation. No product artifacts or new
  checkpoint before this gate.
- **Lanjut AOD / lanjut:** load and reconcile checkpoint and actual sources;
  execute the next dependency-ready action within recorded authorization.
  An unanswered material question remains unanswered.
- **Status AOD:** inspect without writes; report workflow position separately
  from requirement implementation, verification, and UAT acceptance.
- **Jeda AOD:** stop scheduling, safely collect or interrupt active tasks,
  preserve partial output and failure/interruption details, save, explain resume.
- **Ubah mode AOD:** show current scope and choose step, phase-parallel, or
  phase-sequential. Record the new authorization; do not broaden product scope.

## Persistent state

Default: `docs/aod/WORKFLOW_STATE.json`. A compatible project convention may
replace it; record the path. The main agent alone writes state. Read the
[checkpoint contract](references/checkpoint.md) before initialization or recovery.
Use `scripts/workflow.py` for registry validation, read-only inspection, and
revision-checked atomic writes. Do not store secrets or raw sensitive input.

After every unit, use the [handoff contract](references/handoff.md). End with
position, work performed, draft/review/approval status, required decisions,
next action, and whether waiting or continuing. In parallel mode summarize
units and each wave, without internal tool logs.
