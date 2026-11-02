---
name: aod-phase-plan
description: >-
  Builds or revises an evidence-based development plan from the approved Tech
  Spec, product priorities, and relevant system contracts. Use for a phase
  plan, development roadmap, release plan, or implementation sequencing. For
  existing projects, plan remaining work from the observed baseline. Produces
  docs/development/PHASE_PLAN.md.
---

# AOD Development Phase Plan

Turn approved scope into a practical, dependency-aware delivery plan. Follow
`.agents/rules/aod-core.md`. Plan work; do not implement features or invent
scope, dates, effort, or architecture.

## Select planning mode

- **New/planned system:** plan approved work from the starting point described
  in the Tech Spec and Phase Plan request.
- **Existing project:** inspect the current baseline and plan only remaining or
  explicitly approved new work. Use `aod-existing-project-initiation` evidence,
  current code/docs, and user priorities when available.
- **Revision:** preserve completed work and approved sequencing unless new
  evidence or a decision requires changing it. Explain material plan changes.

## Sources and decision rules

Use the approved Tech Spec for technical boundaries; PRD and user decisions for
scope and priority; Data Dictionary, RBAC, State Machine, Business Flow, API
Contract, and UI artifacts for applicable implementation dependencies. Use
existing code and operational evidence for baseline status.

- Do not require every AOD document if irrelevant to the scoped work. Name
  missing inputs and the decisions/tasks they block; continue with independent
  planning where possible.
- Separate approved scope, observed completion, recommendation, estimate, and
  open decision. Never present an inferred priority or estimate as approved.
- Do not schedule a task whose contract or architecture decision is unresolved.
  Show the decision as a prerequisite or explicit decision task.
- Do not re-plan completed features as new deliverables. If completion is
  uncertain, mark it for evidence review rather than assuming either state.

## Build the plan

1. Establish the baseline: project mode, completed/in-progress/unverified work,
   source evidence, and known constraints.
2. Convert approved requirements into traceable work items. Give each item an
   ID, outcome, source references, and acceptance evidence.
3. Map prerequisite relationships across data, lifecycle, authorization,
   interfaces, UI, integrations, and deployment. Use only dependencies that
   affect implementation order.
4. Sequence work by critical dependency, user/business value, risk reduction,
   and release coherence. Prefer vertical slices that can be validated end to
   end; group shared foundations only when they unblock named work.
5. Create phases/releases only where they provide a meaningful milestone. Do
   not force a fixed Phase 0–4 template, sprint length, or parallel workload.
   Parallelize only tasks with independent inputs and low coordination cost.
6. Identify the right implementation route per item: `aod-page-slicer` for an
   approved mock-backed UI page; a feature prompt for backend, integration, or
   end-to-end work; another workflow when the Tech Spec requires it.
7. Add target branch names only when the project adopts a branch convention.
   Label effort/timing as estimates with assumptions and confidence, or omit
   them when evidence is insufficient. Use team capacity or release constraints
   only when provided or evidenced; do not assume a solo/small-team workflow.

## Output: `docs/development/PHASE_PLAN.md`

Use the project's document versioning standard. Include:

1. **Plan Basis** — project mode, scope, source documents, baseline date, and
   approved constraints.
2. **Baseline and Status** — completed, in progress, unverified, and remaining
   items with evidence, especially for existing projects.
3. **Open Decisions and Blockers** — decision, owner, affected items, and what
   can proceed independently.
4. **Dependency Map** — concise table or diagram of the critical dependencies.
5. **Delivery Phases / Releases** — objective, included item IDs, prerequisites,
   outcome, and measurable exit criteria for each meaningful milestone.
6. **Work Item Register** — ID, approved scope, source references, dependencies,
   priority basis, implementation route, acceptance evidence, and status.
7. **Risks and Assumptions** — evidence-based risks and clearly labeled
   planning assumptions; do not turn them into requirements.

For existing projects, number phases as remaining delivery stages if helpful;
do not imply that project setup or completed work must restart. After saving,
identify `aod-feature-prompts` as the next step for work items ready to receive
implementation prompts, or name the missing approval that blocks it.


## Orchestrator handoff

When invoked by `aod-orchestrator`, read
`.agents/skills/aod-orchestrator/references/handoff.md`, return its structured
handoff, and return control to the orchestrator. Do not write workflow checkpoint.
Direct invocation authorizes only the requested scope, not the full workflow.
