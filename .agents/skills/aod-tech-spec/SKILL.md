---
name: aod-tech-spec
description: >-
  Creates or audits a project's Technical Specification: verified stack,
  system boundaries, module responsibilities, data and interface mapping,
  security, operations, and implementation constraints. Use when the user asks
  for a technical specification, tech spec, system architecture, or AOD Phase 4
  development baseline. For an existing codebase, use the as-is baseline mode
  and keep observed architecture separate from proposed target decisions.
---

# AOD Technical Specification

Create a practical, evidence-backed specification that guides implementation
without inventing requirements or overengineering the project. Follow
`.agents/rules/aod-core.md`. The approved Tech Spec is authoritative for
technical architecture; business and interface decisions remain owned by their
respective approved documents.

## 1. Select the Mode and Establish Inputs

### New or planned system

Read the available approved documents and use only those relevant to the
proposed system:

1. PRD for product scope and capabilities.
2. Data Dictionary and DBML for entities and schema.
3. Business Flow and State Machine for behavior and lifecycle.
4. RBAC for identity and authorization requirements.
5. API Contract and UI documents for interface and frontend boundaries.
6. Explicit user decisions for deployment, scale, compliance, integrations, and
   operational constraints.

Do not require an artifact that is irrelevant to the selected architecture. If
an input is missing, identify the decision it affects and continue with
independent sections. Record unresolved choices as open decisions; do not silently
select a stack, database, hosting provider, or architecture pattern.

### Existing project baseline

When preceded by `aod-existing-project-initiation`, describe the current system
from repository evidence before recommending changes. Inspect the relevant
manifest/lockfiles, configuration, routes, modules, data schema, tests, and
deployment files. Treat documentation as evidence of intent, not proof of
implementation.

- Separate **Current State (As-Is)**, **Approved Target State (To-Be)**, and
  **Open Decisions / Recommendations**.
- Mark claims as **Observed**, **Inferred**, **User-Confirmed**, or **Unknown**;
  add repository paths or document sections for material claims.
- Preserve proven versions from manifests and lockfiles. Do not replace them
  with latest versions or recommendations unless the user requested a target
  stack review.
- Record contradictions between code, tests, configuration, and documents
  without deciding product intent on the user's behalf.
- Do not turn a recommendation or gap into an active architecture constraint.

## 2. Verify Technical Facts

- Derive current language, runtime, framework, ORM, database, and package
  versions from repository manifests and lockfiles when available.
- For proposed or uncertain third-party APIs, configuration, and version-specific
  behavior, consult official documentation. Use Context7 when available; use
  the vendor's official documentation otherwise. State the source/version and
  verification date for consequential choices.
- Do not browse or verify every dependency indiscriminately. Ground only choices
  that affect the specification or implementation.
- Never expose secrets. Record configuration keys or secret-management needs,
  not secret values.

If the selected environment does not provide the requested documentation tool,
continue with official vendor documentation when accessible. If neither can be
verified, mark the detail unverified and avoid making it an implementation rule.

## 3. Make Decisions at the Right Level

- Prefer the simplest architecture that meets approved functional and
  non-functional requirements. Do not prescribe microservices, repositories,
  event-driven processing, or a particular layer pattern without a project need.
- Name boundaries and responsibilities using the project's actual framework
  and structure. Adapt examples to the chosen stack; do not copy Laravel
  conventions into Node, Python, Go, or other projects.
- Distinguish **required constraints** from **recommendations**. A constraint
  must have an approved requirement, a user decision, or a concrete technical
  necessity behind it. Explain its source and impact.
- Do not duplicate or redefine business rules, fields, endpoints, permissions,
  or states owned by upstream documents. Map to their IDs/sections where
  possible and report inconsistencies for resolution.
- For an existing project, recommendations for target changes require user
  approval before they become the approved To-Be architecture.

Ask a focused question only when the unresolved choice materially changes
architecture, data, security, operations, cost, or implementation sequencing.
Proceed with unaffected sections and label any non-blocking uncertainty.

## 4. Produce `docs/development/TECH_SPEC.md`

Use the project document versioning standard. Include the sections that apply;
mark unavailable evidence and decisions explicitly rather than filling gaps with
generic boilerplate.

1. **Document Control and Sources** — version/status, inputs, scope, evidence
   date, and material source documents.
2. **System Context and Scope** — purpose, in-scope components, external
   dependencies, constraints, and explicit exclusions.
3. **Current and Target Architecture** — architecture style, application
   boundaries, runtime topology, and a diagram when it clarifies dependencies.
   In existing-project mode, keep As-Is and To-Be distinct.
4. **Verified Technology Stack** — language/runtime, frameworks, database,
   persistence tools, auth, queues, storage, hosting, and versions, each marked
   as observed or approved target.
5. **Module and Integration Boundaries** — responsibilities, ownership, data
   flow, synchronous/asynchronous edges, and failure handling.
6. **Data and Interface Mapping** — map to approved entities and API contracts;
   identify ownership, migrations, validation boundaries, and unresolved gaps.
7. **Security and Privacy** — authentication, authorization, tenant boundaries
   if applicable, sensitive data handling, secrets, audit needs, and relevant
   threat assumptions.
8. **Reliability and Operations** — deployment shape, configuration, logging,
   monitoring, backup/recovery, queues/jobs, retries, timeouts, and availability
   requirements where specified.
9. **Performance and Scale** — known workload, query/index strategy, caching,
   concurrency, and explicit thresholds where available. Do not invent traffic
   targets.
10. **Testing and Delivery** — test layers, required checks, migration/release
    considerations, and environments, aligned with the project's delivery plan.
11. **Architecture Decisions and Constraints** — each entry has decision,
    rationale, source/owner, status (`Approved`, `Proposed`, or `Open`), and
    affected modules.
12. **Risks, Gaps, and Open Questions** — evidence, impact, owner/decision
    needed, and whether the issue blocks implementation.

Map requirements to the modules and technical decisions that implement them.
Avoid prescribing code-level details that belong in a feature prompt unless a
shared constraint must guide multiple features.

## 5. Generate Dynamic Architecture Rules Safely

Create or update `.agents/rules/aod-architecture-engineering.md` and its
documentation mirror `docs/development/ARCHITECTURE_ENGINEERING.md` only when
the user selected the rulebook or selected a Tech Spec that includes approved
operational rules.

- Derive rules only from constraints marked `Approved` in the Tech Spec.
- Keep recommendations and unresolved choices in the Tech Spec; do not place
  them in an active `always_on` rule.
- For a Draft or unapproved Tech Spec, do not activate project-specific rules.
  Leave existing active rules untouched; report the approval needed before
  replacing or enabling them.
- Generate the workspace rule from
  `docs/samples/ARCHITECTURE_ENGINEERING_TEMPLATE.md`, retaining only sections
  relevant to this project's stack and risks.
- Set `trigger: always_on` only when the generated rules are approved and
  intended to govern all coding sessions. Include source sections, scope,
  effective status, and version so agents can trace each active rule.
- Keep the rule concise and operational: state what the agent must do, when the
  rule applies, and the source of authority. Do not duplicate the full Tech Spec.
- Keep the mirror synchronized with the active rule and mark it as a mirror;
  do not maintain two conflicting authorities.
- If an existing dynamic rule differs from the current approved Tech Spec,
  report the delta and update both files together with version history. Preserve
  unrelated local rules and user edits.

If the user requested only a Tech Spec, do not create or change the dynamic
rulebook unless the request or the selected output explicitly includes it.

## 6. Completion and Handoff

Before finishing, check that every active constraint has a traceable source, all
recommendations and open decisions are labeled, As-Is is not presented as an
approved target, and the dynamic rule contains no unapproved policy. Do not
claim tests or documentation verification that was not performed.

After saving the selected deliverables, report the files created or updated,
important open decisions, and the next dependency-aware action. The usual next
step is `aod-phase-plan` when a usable Tech Spec is ready.


## Scoped changes

For an initialized product change, read
`.agents/skills/aod-orchestrator/references/change-workflow.md`
and follow its minimum section-level delta and single-authorization contract.
The existing approved baseline and accepted change plan supply relevant inputs;
do not require full bootstrap generation or duplicate document approvals.
Preserve material unresolved decisions. This does not broaden audit-only scope.

## Orchestrator handoff

When invoked by `aod-orchestrator`, read
`.agents/skills/aod-orchestrator/references/handoff.md`, return its structured
handoff, and return control to the orchestrator. Do not write workflow checkpoint.
Direct invocation authorizes only the requested scope, not the full workflow.
