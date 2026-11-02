---
name: aod-orchestrator
description: >-
  Guides AI-Orchestrated Development (AOD) for new and existing software
  projects. Use when the user says "start AOD", "mulai AOD", "setup project
  AOD", "panduan AOD", "where am I in AOD", or asks which AOD step comes
  next. Inspects existing project artifacts, identifies the correct workflow
  path, checks prerequisites, and routes work to the relevant AOD skill without
  repeating completed steps or inventing missing decisions.
---

# AOD Master Orchestrator

Guide the user through AOD and select the smallest valid next step for the
project's actual state. Follow `.agents/rules/aod-core.md` as the governing
workflow policy. This skill coordinates work; specialist skills create their
own artifacts.

## On Activation

1. Inspect the project root for AOD documents, agent instructions, and relevant
   repository context before asking questions.
2. Classify the project path:
   - **New project:** no meaningful application implementation exists yet.
   - **Existing project:** application code or operational modules already
     exist; start with `aod-existing-project-initiation`.
   - **Active AOD project:** AOD artifacts exist; resume from the earliest
     incomplete dependency relevant to the user's request.
3. Present a short status: identified path, current phase or baseline, available
   documents, missing prerequisites, and one recommended next action.
4. Ask only for information that cannot be established from the repository or
   prior approved decisions. Do not repeat questions already answered.
5. Activate the relevant specialist skill when its prerequisites are met. If
   the requested task is blocked, explain the specific missing input and offer
   an unblocked next action.

Do not begin by asking the user to choose a phase when repository evidence can
answer that question. Do not create documents during an existing-project
screening; that screening is read-only and follows
`aod-existing-project-initiation`.

## AOD Workflow Map

### Optional Pre-Project

- `aod-proposal` — create a commercial proposal from available business and
  technical context. Label pricing or timeline estimates that lack approved
  inputs as estimates.

### Phase 1 — Business Layer

1. `aod-brd` — business problem, objectives, scope, stakeholders, risks.
2. `aod-business-flow` — current and target workflows.
3. `aod-prd` — approved product scope and requirements.
4. After the PRD, prepare the applicable artifacts; independent documents may
   proceed in parallel:
   - `aod-flowchart` from Business Flow.
   - `aod-rbac` from PRD and workflow actions.
   - `aod-data-dictionary` from PRD; then `aod-dbml` from the dictionary.

### Phase 2 — System Design

After the relevant business requirements are available:

- `aod-state-machine` — lifecycle and allowed transitions.
- `aod-api-contract` — HTTP interface contract for APIs, web routes, or a
  developer-confirmed mix, grounded in PRD, data, and the Tech Spec.
- `aod-ui-flow` — screens, journeys, visibility, and actions.
- `aod-website-concept` — product and UX direction from business context.
- `aod-design-system` — visual principles and component standards.
- `aod-ui-style` — concrete tokens based on the concept and design system.

The API Contract and UI Flow can be drafted in parallel when both have the
required inputs. Before defining route types or auth/response behavior,
`aod-api-contract` must inspect the Tech Spec and confirm the API, web-route,
or mixed mode with the developer. Do not make a downstream contract
authoritative while its upstream requirements or this interface decision
remain unresolved.

### Phase 3 — UI Architecture

Complete the design and implementation plans for the UI; this phase does not
authorize page code by itself.

1. `aod-ui-component-map` — page and component structure.
2. `aod-ui-slicing` — layouts, mock schemas, page skeletons, and UI states.
3. `aod-tailwind-config` — Tailwind or equivalent token configuration.

These artifacts feed the Technical Specification and Phase Plan. The
`aod-page-slicer` skill writes page code, so route it to Phase 4 implementation
after the relevant design artifacts, Technical Specification, and Phase Plan
are approved.

### Phase 4 — Development

1. `aod-tech-spec` — implementation architecture and project-specific rules.
2. `aod-phase-plan` — remaining work ordered by dependencies and priority.
3. `aod-feature-prompts` — atomic prompts for approved features.
4. `aod-dod` — feature completion criteria before implementation begins.
5. Implement one approved unit at a time:
   - `aod-page-slicer` for a scoped, mock-backed UI page.
   - The relevant feature prompt and coding workflow for backend, integration,
     or end-to-end functionality.
6. After each implementation, run relevant checks, update ARC and its registry,
   and validate the feature against DoD before calling it complete.

Use `aod-quick-checklist` for a focused terminal checklist and
`aod-progress-tracker` for a requirement-to-code audit. Keep their default
terminal output ephemeral; export a report only when the user requests a file.

### Phase 5 — Testing and Delivery

- `aod-uat` — generate stakeholder test scenarios from approved requirements,
  workflows, UI Flow, and State Machine.
- Report verification evidence and unresolved gaps. Do not claim deployment,
  stakeholder acceptance, or tests passed without evidence.

### Maintenance and Revisions

- `aod-feedback-loop` — classify feedback, assess upstream impact, plan the
  revision, and guide approved changes through verification and final reporting.

## Routing and Phase Gates

- Check the selected skill's own prerequisites and the project state before
  routing. The phase map is a dependency guide, not a demand to generate every
  possible artifact in every project.
- For a **new project**, follow the dependencies above and make unresolved
  business or architecture choices visible before they affect downstream work.
- For an **existing project**, use `aod-existing-project-initiation` first.
  Establish an evidence-based as-is baseline, then let the user choose relevant
  documents or implementation planning. Do not force missing bootstrap
  documents or a full Phase 1–5 replay.
- For an **active project**, preserve valid approved decisions and completed
  work. Continue from the earliest unmet prerequisite relevant to the requested
  task; do not regenerate artifacts merely to follow numbering.
- A missing input blocks only work that depends on it. Identify the missing
  artifact or decision, why it matters, and any independent work that can
  continue.
- Distinguish **observed fact**, **inference**, **working assumption**, and
  **open decision**. Drafts may contain labeled low-risk assumptions; do not
  implement consequential open decisions.
- Ask for clarification only when an unresolved choice materially affects
  business behavior, scope, data, access, lifecycle, security, integration, or
  architecture. Respect explicit decisions already given by the user.
- Before revising a feedback or change-request document, use the planning gate in
  `aod-feedback-loop` and follow the user's approval before dependent edits.

## Navigation Requests

- **"next step" / "lanjut"** — show the next valid action and route to its
  skill if inputs are ready.
- **"where am I" / "fase berapa"** — report phase, completed artifacts, active
  work, and the next unmet dependency from repository evidence.
- **"what do I need" / "apa yang dibutuhkan"** — list only prerequisites for
  the selected next task.
- **"quick checklist" / "checklist phase" / "checklist slicing"** — route to
  `aod-quick-checklist`.
- **"cek progress" / "report progress"** — route to `aod-progress-tracker`.

## Parallel Work Guidance

Parallelize only artifacts that have all required inputs and do not depend on
one another's unresolved decisions. Common examples after an approved PRD are
RBAC, Data Dictionary, State Machine, and UI Flow. DBML follows the Data
Dictionary; Design System follows Website Concept; UI Style follows both the
Concept and Design System. When one artifact changes an upstream decision,
recheck dependent artifacts before implementation.
