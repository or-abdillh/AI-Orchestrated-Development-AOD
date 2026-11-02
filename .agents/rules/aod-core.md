---
trigger: always_on
---

# AOD Core Rules — Always Active

These rules govern AOD work in every project. Use the project's current state and the task's scope to select the applicable path; do not force a new-project workflow onto an existing codebase.

## 1. Select the Project Path

- **New project:** Start with business discovery and follow the dependency map below.
- **Existing project:** Start with `aod-existing-project-initiation`. Its initial repository screening is read-only. Record observed facts, inferences, unknowns, conflicts, and evidence separately. Do not require missing bootstrap documents to describe the current system.
- **Focused task in an initialized project:** Inspect the relevant project documents and code, identify the active phase and unmet prerequisites, then continue from the nearest valid step. Do not regenerate completed upstream work without a reason.
- A user may choose a narrower deliverable. Produce only the requested artifact when its required inputs are available; explain material gaps and avoid fabricating decisions.

## 2. Workflow and Dependency Rules

Follow this dependency-aware sequence. Items in the same group may be prepared in parallel once their shared inputs are ready.

1. **Business discovery:** Study Case → BRD and Business Flow → PRD.
2. **Business and system contracts:** After PRD, prepare the relevant Flowchart, RBAC, Data Dictionary, State Machine, API Contract, and UI Flow. DBML depends on the Data Dictionary. Website Concept depends on business context and informs Design System; UI Style depends on Website Concept and Design System.
3. **UI architecture:** UI Component Map depends on UI Flow and the relevant product, design, state, and API documents. UI Slicing depends on the Component Map, Design System, UI Style, API Contract, and State Machine. Tailwind or equivalent token configuration depends on UI Style.
4. **Development readiness:** Technical Specification depends on the approved product and system contracts relevant to implementation. Phase Plan depends on the Technical Specification and uses available UI and workflow specifications. Feature Prompts and DoD depend on the approved implementation plan and applicable contracts.
5. **Implementation:** Implement one scoped feature or page at a time only after its required upstream contracts are approved and a valid Phase Plan exists. `aod-page-slicer` may implement a mock-backed UI page, but it is still implementation and follows this gate.
6. **Verification and delivery:** Run applicable automated checks, validate DoD, and prepare UAT from the approved requirements and workflows.

Do not interpret this sequence as requiring every possible document for every project. A skill's stated prerequisites and the current task determine the minimum inputs. If a prerequisite is missing, name it and its impact; proceed with independent, unblocked work where useful. Pause only the decision or implementation that depends on unresolved information.

## 3. Approval, Assumptions, and Decision Boundaries

- The user owns product scope, business rules, and architecture decisions. The agent may analyze options and make recommendations, but must label them as recommendations until accepted.
- Never present an inference, assumption, or recommendation as an observed fact or approved decision.
- A document may contain clearly labeled, low-risk working assumptions to make a draft useful. Mark consequential, ambiguous, or conflicting items as open decisions. Do not implement or treat an open decision as an approved requirement.
- Ask a focused clarification when an unresolved choice materially changes scope, data, permissions, lifecycle, security, integration, or architecture. Do not block unrelated work on that question.
- Treat explicit user decisions in the current project documents or conversation as authorization; do not ask again unless new evidence creates a material conflict.
- Do not expand scope or make irreversible external changes without explicit authorization.

## 4. Document Authority and Conflict Resolution

Use each document as authority for its domain:

| Decision area                                                              | Authority                                                           |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Business goals, stakeholders, and boundaries                               | BRD; Study Case is source context                                   |
| Product scope, features, and acceptance intent                             | Approved PRD                                                        |
| Operational behavior and actors                                            | Approved Business Flow                                              |
| Roles and permissions                                                      | RBAC                                                                |
| Entities, fields, types, and relationships                                 | Data Dictionary                                                     |
| Entity lifecycle and valid transitions                                     | State Machine                                                       |
| HTTP interfaces (API endpoints or web routes) and request/response schemas | API Contract                                                        |
| Visual tokens and component standards                                      | Design System and UI Style                                          |
| Technical architecture and implementation conventions                      | Approved Technical Specification and its project architecture rules |
| Work order, deliverables, and phase exit criteria                          | Approved Phase Plan                                                 |

When documents conflict, do not resolve the conflict by a universal document ranking. Preserve each source, identify the affected decision, and ask the project owner to resolve it. Until resolved, follow the last explicitly approved decision only where it remains unambiguous and do not implement the conflicting part. Downstream documents must reflect the relevant upstream authority; they do not silently redefine it.

Never invent database fields, endpoints, enum values, permissions, or state transitions. Propose additions in the owning document and wait for approval before implementing them.

## 5. Implementation Guardrails

- Implement only the approved scope of the active feature prompt or user task. Follow the approved Technical Specification and project-specific architecture rules.
- Before modifying an existing feature, inspect its relevant code and read any matching Agent Reference Context (ARC) documents.
- Keep business logic, validation, persistence, and authorization in the layers defined by the project's architecture. Do not impose a framework-specific pattern when the Tech Spec does not select it.
- Use official, version-matched documentation for third-party APIs and configuration. Use Context7 when available; otherwise use the library's official documentation. Record a limitation if neither source can be verified.
- For UI work, follow the approved Design System and UI Style. If a required token or component is missing, propose the upstream design change instead of inventing a conflicting style.
- In a Git-managed project, follow its established branch and commit workflow. If AOD branch conventions are adopted, use a dedicated phase/feature branch and do not commit implementation directly to `main` or `master`.

## 6. Document Lifecycle

For documents generated or revised in `docs/`, use the project's document versioning standard: semantic version, last-updated date, status, generator/author, and revision history. On edits, update the version and revision history according to the size and compatibility of the change. Do not add AOD version metadata to unrelated files or modify documents outside the requested scope.

For client feedback or change requests, use `aod-feedback-loop` to assess scope and downstream impact. Follow its planning and clarification gate before dependent edits or code changes. Update approved upstream contracts before implementing affected code, then record the outcome in the required final report.

## 7. Definition of Done and Continuity

A task is complete when its acceptance criteria are met, relevant checks have been run or their absence is stated, and required project documentation is updated. For Phase 3/4 implementation, create or update the applicable ARC reference and `docs/references/INDEX.md` as required by the project's DoD. Do not claim tests passed unless they were run and their result is available.

## 8. Standard Output Locations

- BRD, Business Flow, PRD, Flowchart, RBAC, Data Dictionary, DBML: `docs/business/`
- State Machine, API Contract, UI Flow, Website Concept, Design System, UI Style: `docs/system-design/`
- Component Map, UI Slicing, Design Tokens: `docs/ui-architecture/`
- Technical Specification, Phase Plan, Feature Prompts, DoD, Progress Report: `docs/development/`
- UAT: `docs/testing/`
- Proposal: `docs/proposal/`
- Feedback and final reports: `docs/feedback/`
- UI and feature references plus registry: `docs/references/`

Use an existing project convention when one is already established and compatible; report any material deviation from these defaults.
