<!-- antislop:start -->

## antislop

For UI, copy, people, mobile layout, or code comments work, load the antislop skill for the task:

- Core filter, always on: `antislop`
- UI / visual: `antislop-ui`
- Copy & text: `antislop-copywriting`
- Code comments: `antislop-code`
- Mobile / responsive: `antislop-layoutmobile`
- People: `antislop-human`
Before starting, ask the user when antislop applies: during the work, or after it is done.
<!-- antislop:end -->

<!-- aod:start -->
## AI-Orchestrated Development (AOD)

Use `aod-orchestrator` for **Mulai AOD**, **Lanjut AOD / lanjut**, **Status AOD**,
**Jeda AOD**, and **Ubah mode AOD**. Read its SKILL.md, registry and protocol;
execute the selected specialist and return control. Do not require developers
to remember specialist names. Direct specialist calls remain limited in scope.

Before changes, read `.agents/rules/aod-core.md`, relevant ARC references,
approved contracts and project architecture rules. Initial inspection is
read-only. Show workflow overview and obtain explicit start confirmation;
choose step, phase-parallel or phase-sequential mode before each phase.
Use available question box or numbered chat fallback; silence is not approval.
Only the main orchestrator writes `docs/aod/WORKFLOW_STATE.json`. Reconcile
sources and approvals on resume; never infer approval from file existence.
Preserve existing-project screening and valid as-is work. Phase 3 creates UI
plans; Phase 4 implements them. Follow approved Tech Spec/Phase Plan, DoD and
ARC. API/web/mixed is developer-confirmed; never assume Sanctum or Tailwind.
Design System/UI Style remain framework-neutral; styling adapter is optional
planned Phase 4 work. Proposal requires stable approved PRD and Tech Spec.
Use Context7 for third-party implementation documentation. Keep architecture
rules derived only from approved constraints. Feedback updates affected upstream
sources first. Quick Checklist is read-only; Progress Tracker audits evidence
and exports only on request. Workflow completion is not product/UAT acceptance.
Documents under docs use SemVer, Last Updated and Revision History; JSON state
uses schema/revision metadata. Use feature branches and smart-git-commit.

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
