<!-- aod:start -->
## AI-Orchestrated Development (AOD)

Use `aod-orchestrator` for **Mulai AOD**, **Lanjut AOD / lanjut**, **Status AOD**,
**Jeda AOD**, and **Ubah mode AOD**. Read its SKILL.md, registry and protocol;
execute the selected specialist and return control. Do not require developers
to remember specialist names. Direct specialist calls remain limited in scope.

Before changes, read core rules, relevant project contracts and ARC.
First classify the task: guided new-project discovery, existing adoption, or
scoped fix/feature/module change. For changes use the scoped change protocol;
no replay of phases 0–5. One accepted plan authorizes its document deltas,
implementation, checks and final documentation. Clear apply instructions
already authorize in-scope work. Ask only for unresolved material decisions or
separately authorized actions; never fabricate developer document sign-off.
Per-phase start/mode/review gates apply only to guided discovery or when the
developer explicitly requests them. Reuse session parallelism preferences.
Read the change-workflow reference before invoking specialist generators.
Patch only affected contract sections before dependent code, then synchronize
implementation facts, ARC and required docs after verification. No compulsory
full Phase Plan/Feature Prompt regeneration for a focused change.
Preserve baseline checkpoints; scoped changes may use docs/aod/changes/<id>.json.
Source hash differences require impact assessment, not automatic re-approval.
Only the main agent writes state. Question box has a numbered-chat fallback;
no response never approves a material decision. Preserve existing API/web/mixed,
framework-neutral tokens and approved architecture; never assume Sanctum or
Tailwind. DoD, actual verification, documentation and ARC remain completion
criteria. Quick Checklist is read-only; Progress Tracker independently audits
and exports only on request. UAT preparation is not stakeholder acceptance.

Use `.agents/aod/bin/arc` for deterministic list/search/trace/check/graph ARC
navigation without AI overhead. Preserve stable metadata IDs and explicit
source relations when updating ARC. INDEX owns registration; references own
identity and connections. Run arc check for impacted references; do not treat
CLI structural checks as semantic verification or invent links/approvals.

### Workflow map (generated from registry)
<!-- aod:map:start -->
| Phase | Steps / executing skills |
| --- | --- |
| 0 — Discovery / Baseline | `discovery`, `aod-existing-project-initiation` |
| 1 — Business Layer | `aod-brd`, `aod-business-flow`, `aod-prd`, `aod-flowchart`, `aod-rbac`, `aod-data-dictionary`, `aod-dbml` |
| 2 — System Design | `aod-state-machine`, `aod-api-contract`, `aod-ui-flow`, `aod-website-concept`, `aod-design-system`, `aod-ui-style` |
| 3 — UI Architecture | `aod-ui-component-map`, `aod-ui-slicing` |
| 4 — Development | `aod-tech-spec`, `aod-phase-plan`, `aod-feature-prompts`, `aod-dod`, `aod-tailwind-config`, `implementation` |
| 5 — Testing | `aod-uat` |
<!-- aod:map:end -->
<!-- aod:end -->
