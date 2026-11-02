---
name: aod-feature-prompts
description: >-
  Creates a library of scoped, reusable implementation prompts for approved
  Phase Plan work items. Use for a feature prompt library or coding prompts
  tied to a delivery plan. Requires an approved Tech Spec and Phase Plan plus
  the applicable product and interface contracts. Produces
  docs/development/FEATURE_PROMPTS.md.
---

# AOD Feature Prompt Library

Translate ready Phase Plan work items into prompts an AI coding agent can
execute with minimal ambiguity. This skill creates prompts only; it does not
implement code. Follow `.agents/rules/aod-core.md` and adapt every instruction
to the approved project architecture.

## Inputs and readiness

Read the approved Technical Specification and Phase Plan first. For each work
item, load only relevant sources: PRD/Business Flow, Data Dictionary/DBML,
RBAC, State Machine, API Contract, UI Flow, Component Map, UI Slicing,
Design System/UI Style, ARC references, and DoD.

- Generate prompts only for approved, scoped work items. Preserve Phase Plan
  IDs, dependencies, acceptance criteria, and implementation route.
- If required scope, contract, permission, lifecycle, or architecture is
  unresolved, mark the prompt **Blocked** and name the exact decision. Do not
  hide the gap behind generic wording or ask the coding agent to guess.
- Distinguish observed repository conventions from approved target decisions.
  In existing projects, require inspection of current code and preservation of
  unrelated/local changes.
- Route an approved mock-backed UI page to `aod-page-slicer`; do not duplicate
  its page implementation workflow as a generic backend prompt. Use a feature
  prompt for backend, integration, or end-to-end work as scoped by the plan.

## Prompt design rules

Each prompt must describe one bounded work item and include:

1. **Identity and scope** — prompt ID, Phase Plan item ID, feature/module, goal,
   explicit inclusions and exclusions.
2. **Approval gate** — required Tech Spec/Phase Plan status and upstream
   decisions. Stop only the affected work when a prerequisite is missing.
3. **Source map** — exact document sections/requirement IDs, field names,
   permissions, transitions, interface operations, and ARC links that apply.
4. **Repository discovery** — inspect stack/version, existing implementation,
   conventions, relevant references, and current local changes before editing.
5. **Implementation plan** — concise, dependency-aware tasks based on the
   project's actual layers and feature type. Include migration/schema changes
   only when the approved work item changes the Data Dictionary; use the
   project's actual validation, domain, persistence, route, and authorization
   mechanisms. Do not prescribe Laravel MVC, Service classes, API Resources,
   DTOs, or repository patterns to projects that do not use them.
6. **Behavior and constraints** — approved business rules, validation,
   authorization, states, interface behavior, accessibility/design rules when
   UI is in scope, and explicit non-goals.
7. **Verification and completion** — checks specified by the Tech Spec/Phase
   Plan/DoD, acceptance evidence, applicable ARC updates, and a factual report
   of checks actually run. Never claim unperformed checks passed.

Add branch instructions only when the project has adopted a branch workflow;
then use the Phase Plan or repository convention. Do not make a Git command,
branch name, commit, Context7, or a particular test framework universal. Apply
`.agents/rules/aod-core.md` and relevant local instructions for those choices.

Do not put unrelated features, future integrations, speculative fields, or
unapproved fixes in a prompt. If implementing the feature reveals a contract
conflict, pause that dependent change, report the evidence, and continue
independent in-scope work where safe.

## Output: `docs/development/FEATURE_PROMPTS.md`

Use the project's document versioning standard. Organize prompts in Phase Plan
order, with a short index mapping prompt ID to work item, dependencies, status
(Ready/Blocked), and source. Keep each copy-ready prompt self-contained but
concise. Include a brief shared instruction block only for rules common to all
prompts; do not repeat entire upstream documents.

Before saving, check coverage: every ready implementation work item has one
prompt or an explicit reason for omission; blocked items identify the missing
decision; no prompt expands the approved scope. After saving, identify
`aod-dod` as the next step when DoD has not yet been prepared.


## Orchestrator handoff

When invoked by `aod-orchestrator`, read
`.agents/skills/aod-orchestrator/references/handoff.md`, return its structured
handoff, and return control to the orchestrator. Do not write workflow checkpoint.
Direct invocation authorizes only the requested scope, not the full workflow.
