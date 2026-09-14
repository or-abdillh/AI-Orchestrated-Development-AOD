# AOD Core Rules — Always Active

> These rules are always active in every AOD project session.
> AI must follow these guardrails without exception.

---

## Phase Discipline / Disiplin Fase

- NEVER skip phases. The AOD sequence must be followed:
  Business Layer → System Design → UI Architecture → Development → Testing
- Tidak boleh melompat fase. Jika dokumen prerequisite belum ada, STOP dan minta user melengkapinya.
- NEVER assume data not present in the provided documents.
- NEVER generate implementation code unless Technical Specification AND Phase Plan are finalized.
- ALWAYS ask for clarification before proceeding if a required document is missing.

## Document Dependency Chain / Rantai Dependensi

BRD → Business Flow → PRD → (RBAC, Data Dictionary, State Machine, API Contract, UI Flow) → Tech Spec → Phase Plan → Feature Prompts → DoD → UAT

Each document depends on the previous one. Do not produce downstream artifacts without upstream artifacts.

## AI Role in AOD / Peran AI dalam AOD

- AI is the EXECUTOR, not the ARCHITECT.
- AI does not make architecture decisions.
- AI does not change scope without user approval.
- AI does not introduce patterns not defined in the Technical Specification.
- Jangan improvisasi fitur atau skema database yang tidak didefinisikan.

## Document Priority Rules (Universal)

When multiple documents conflict:
1. Technical Specification > PRD > Business Flow > BRD > Study Case
2. Data Dictionary adalah single source of truth untuk semua field dan entitas.
3. API Contract adalah single source of truth untuk semua endpoint.
4. Never invent fields not defined in the Data Dictionary.
5. Never create endpoints not defined in the API Contract.

## Output Naming Convention

Save all generated documents to `docs/` within the project directory:
- BRD → `docs/business/BRD.md`
- Business Flow → `docs/business/BUSINESS_FLOW.md`
- PRD → `docs/business/PRD.md`
- Flowchart → `docs/business/FLOWCHART.md`
- RBAC → `docs/business/RBAC.md`
- Data Dictionary → `docs/business/DATA_DICTIONARY.md`
- DBML → `docs/business/SCHEMA.dbml`
- State Machine → `docs/system-design/STATE_MACHINE.md`
- API Contract → `docs/system-design/API_CONTRACT.md`
- UI Flow → `docs/system-design/UI_FLOW.md`
- Website Concept → `docs/system-design/WEBSITE_CONCEPT.md`
- Design System → `docs/system-design/DESIGN_SYSTEM.md`
- UI Style → `docs/system-design/UI_STYLE.md`
- UI Component Map → `docs/ui-architecture/COMPONENT_MAP.md`
- UI Slicing → `docs/ui-architecture/UI_SLICING.md`
- Tech Spec → `docs/development/TECH_SPEC.md`
- Phase Plan → `docs/development/PHASE_PLAN.md`
- Feature Prompts → `docs/development/FEATURE_PROMPTS.md`
- DoD → `docs/development/DOD.md`
- UAT Sheet → `docs/testing/UAT_SHEET.md`
- Proposal → `docs/proposal/PROPOSAL.md`

## Document Versioning & Tracking / Standar Versi Dokumen

- EVERY document created in `docs/` MUST include version metadata at the top:
  - Version: `vMAJOR.MINOR.PATCH` (e.g. `v1.0.0`)
  - Last Updated: `YYYY-MM-DD`
  - Status: `Draft` | `In Review` | `Approved` | `Superseded`
  - Author / Generator: Skill name
  - Revision History table
- AI MUST bump the version upon ANY update:
  - MAJOR (`vX.0.0`): Fundamental architectural change, breaking scope alteration, or complete rework.
  - MINOR (`v1.X.0`): Additions of new modules, features, entities, or endpoints that are backward-compatible.
  - PATCH (`v1.0.X`): Text clarifications, formatting improvements, typo fixes, or minor notes.
- AI MUST update the `Last Updated` date and append an entry to the `Revision History` log on every revision.
- Never edit an existing document without bumping version and updating history.

## Git Feature-Branching Enforcement / Disiplin Branching Git

- In Phase 4 (Development), NEVER commit implementation code directly to `main` or `master`.
- Every Phase must have a dedicated branch: `phase/<phase-num>-<phase-slug>` (e.g. `phase/01-core-foundation`).
- Every Feature must have a dedicated branch: `feat/<module>-<feature-slug>` (e.g. `feat/orders-create-order`).
- AI must ensure the workspace is on the correct feature branch before generating code.
- AI must validate against `aod-dod` before completing the feature branch.
- Atomic commits must be executed via `smart-git-commit`.


