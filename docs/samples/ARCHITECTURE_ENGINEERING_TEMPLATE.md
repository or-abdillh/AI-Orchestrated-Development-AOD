# Project Architecture Rules: [Project Name]

> **Version:** `v1.0.0`
> **Last Updated:** `YYYY-MM-DD`
> **Status:** `[Draft until project owner approves the rules]`
> **Approved By:** `[Project owner / decision reference]`
> **Authority Source:** `docs/development/TECH_SPEC.md#[section]`
> **Rule Scope:** `[all implementation / named modules / named workflows]`
> **Framework and Version:** `[verified or approved stack]`

---

## Revision History

| Version | Date | Author / Generator | Description |
|---|---|---|---|
| `v1.0.0` | `YYYY-MM-DD` | `aod-tech-spec` | Initial rules derived from approved Technical Specification. |

---

> Generate this file only from decisions marked **Approved** in the Technical
> Specification. Delete this note and every section that does not apply. Do not
> promote examples, assumptions, recommendations, or unresolved decisions into
> active rules.

## 1. Active Architecture Constraints

| Constraint | Required agent behavior | Applies to | Tech Spec source |
|---|---|---|---|
| `[Approved constraint]` | `[Concrete action or prohibition]` | `[Module/workflow]` | `[#section]` |

## 2. Project Boundaries and Layer Responsibilities

Document only boundaries selected for this project. Use actual directory names
and framework terms. If the project does not prescribe a layer or pattern, do
not invent one here.

| Boundary / Layer | Responsibility | May depend on | Must not do | Source |
|---|---|---|---|---|
| `[Observed or approved boundary]` | `[Responsibility]` | `[Allowed dependencies]` | `[Forbidden dependency, if approved]` | `[#section]` |

## 3. Data, Transactions, and Concurrency

Include only rules required by approved data integrity, workload, or concurrency
decisions. Reference the Data Dictionary and relevant design decision. Do not
apply database-specific mechanisms to another database without verification.

- **Schema authority:** `docs/business/DATA_DICTIONARY.md` `[or project equivalent]`
- **Approved transaction/concurrency rules:** `[rule, scope, source; or "None specified"]`
- **Migration/backward-compatibility constraints:** `[approved rule; or "None specified"]`

## 4. Interfaces, Security, and Integrations

- **API/interface authority:** `[API Contract path, or "Not applicable"]`
- **Authorization and sensitive-data rules:** `[approved rules and source]`
- **Integration boundaries, retries, and failure behavior:** `[approved rules and source]`
- **Secret handling:** Never copy secret values into code, documentation, or logs.

## 5. Frontend and Design Rules (When Applicable)

- **Design authority:** `[Design System and UI Style paths, or "Not applicable"]`
- **Component, state, accessibility, and responsive requirements:** `[approved constraints]`
- Do not invent visual tokens or component standards when the design documents
  are silent; record the gap for resolution.

## 6. Verification and Delivery Constraints

- **Required checks:** `[commands or procedures approved for this project]`
- **Migration, deployment, or rollback constraints:** `[approved rules]`
- **Completion evidence:** `[test, review, or operational evidence required]`

## 7. Open Decisions and Recommendations

This section is informational and is not an active rule. Move an item into an
active section only after the decision is approved in the Tech Spec and this
rulebook is regenerated.

| Item | Recommendation or question | Decision owner | Blocking scope |
|---|---|---|---|
| `[Open item]` | `[Details]` | `[Owner]` | `[Affected work]` |
