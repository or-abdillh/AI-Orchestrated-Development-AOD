# User Acceptance Test Sheet

> **Version:** `v1.0.0`
> **Last Updated:** `YYYY-MM-DD`
> **Status:** `[Draft / Ready for UAT / In Execution / Accepted / Rejected]`
> **Project / Release:** `[name, release/build or Unknown]`
> **Prepared By:** `aod-uat`

## Revision History

| Version  | Date         | Author    | Change            |
| -------- | ------------ | --------- | ----------------- |
| `v1.0.0` | `YYYY-MM-DD` | `aod-uat` | Initial UAT sheet |

## 1. Scope and Sources

- **In scope:** `[approved feature/release scope]`
- **Out of scope:** `[explicit exclusions or None specified]`
- **Sources:** `[PRD requirements, Business Flow, RBAC, State Machine, UI Flow, BRD sections]`
- **Test environment / build:** `[value or Unknown]`
- **Coverage limitations / setup needs:** `[items or None]`

## 2. Requirement Coverage Matrix

| Requirement / Acceptance ID | Requirement summary  | Scenario IDs | Coverage (`Covered / Partial / Blocked / N/A`) | Gap / reason      |
| --------------------------- | -------------------- | ------------ | ---------------------------------------------- | ----------------- |
| `[source ID or section]`    | `[approved outcome]` | `[UAT-...]`  | `[status]`                                     | `[reason or N/A]` |

## 3. UAT Scenario Register

| Scenario ID        | Requirement ID(s) | Feature / workflow   | Screen              | Actor role    | Preconditions / initial state          | Test data             | Test steps                     | Expected result / final state                         | Priority                | Actual result / evidence | Tester / date | Status    |
| ------------------ | ----------------- | -------------------- | ------------------- | ------------- | -------------------------------------- | --------------------- | ------------------------------ | ----------------------------------------------------- | ----------------------- | ------------------------ | ------------- | --------- |
| `UAT-[module]-001` | `[REQ-ID]`        | `[approved feature]` | `[screen/workflow]` | `[RBAC role]` | `[precondition/state or N/A + reason]` | `[synthetic fixture]` | `1. [action]`<br>`2. [action]` | `[observable result; expected state or N/A + reason]` | `[High / Medium / Low]` |                          |               | `Not Run` |

## 4. Role and State Coverage

| Role / actor  | Requirement / allowed action | Scenario IDs | Coverage / gap                  |
| ------------- | ---------------------------- | ------------ | ------------------------------- |
| `[RBAC role]` | `[source-backed action]`     | `[UAT IDs]`  | `[Covered / Partial / Blocked]` |

| Entity            | Initial state | Actor and action | Guard / precondition | Expected state | Scenario ID |
| ----------------- | ------------- | ---------------- | -------------------- | -------------- | ----------- |
| `[entity or N/A]` | `[state]`     | `[role/action]`  | `[condition]`        | `[state]`      | `[UAT ID]`  |

## 5. Execution Summary and Sign-off

| Metric                              | Count / decision                                             |
| ----------------------------------- | ------------------------------------------------------------ |
| Scenarios executed                  | `[n / total]`                                                |
| Passed / Failed / Blocked / Not Run | `[counts]`                                                   |
| Business decision                   | `[Pending / Accepted / Accepted with conditions / Rejected]` |
| Open defects / decisions            | `[IDs or None]`                                              |

| Stakeholder / role | Decision                      | Conditions / notes | Date     |
| ------------------ | ----------------------------- | ------------------ | -------- |
| `[name or role]`   | `[Pending / Accept / Reject]` | `[notes]`          | `[date]` |

## 6. Open Decisions and Blockers

- `[item, owner, impact on UAT; or None]`
