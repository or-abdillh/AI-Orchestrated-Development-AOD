---
name: aod-api-contract
description: >-
  Defines the application's HTTP interface contract, including API endpoints,
  web routes, or a confirmed mix, with request, response, validation, and
  authorization behavior. Use for API design, route definitions, endpoint
  contracts, or the AOD API Contract. Requires PRD and Data Dictionary; inspect
  the approved Tech Spec when available and obtain the developer's route-mode
  confirmation before specifying interfaces. Produces
  docs/system-design/API_CONTRACT.md.
---

# AOD Application Interface Contract

Define the contract between application capabilities and their HTTP consumers.
Despite the conventional filename `API_CONTRACT.md`, the artifact may describe
JSON APIs, ordinary web routes, or both. Follow `.agents/rules/aod-core.md`.
Never assume every interaction must be a REST API.

## Sources and authority

- Use the approved PRD for capabilities and operations.
- Use Data Dictionary for field names and types; Business Flow and State
  Machine for timing, actors, and lifecycle behavior; RBAC for access rules.
- Read the approved Technical Specification when available and inspect
  existing project architecture before proposing route or transport details.
  If no Tech Spec exists yet, say so; use the developer's confirmed route mode
  for a framework-neutral draft and leave stack-specific details open. In an
  existing project, record observed conventions separately from target
  decisions.
- The Tech Spec informs the recommendation but does not replace the required
  developer confirmation of route mode.
- Do not invent operations, fields, enum values, auth mechanisms, response
  formats, versioning schemes, or framework features.

## Required developer confirmation

Before deciding the contract's interface style, present the evidence found in
the Tech Spec/project and ask the developer to select one:

1. **API for all operations** — specify API endpoints and API response/auth
   behavior.
2. **Web routes for all operations** — specify browser-oriented routes and
   their page/form response behavior.
3. **Mixed** — identify which operations use API and which use web routes.

Ask directly, for example: _"Tech Spec/codebase menunjukkan [evidence]. Untuk
contract ini, konfirmasi: semua operasi memakai API, semua memakai web routes,
atau campuran? Jika campuran, operasi mana untuk masing-masing?"_ Do not infer
the answer from Laravel, a frontend framework, or the presence of Sanctum.

Ask this even when the Tech Spec suggests a mode; state the evidence and a
recommended choice so the developer can confirm or override it. Record the
answer and its scope in the contract. If unanswered, do not finalize route
types, authentication, or response formats. Continue only with route-neutral
operation and data analysis, and mark the interface decision as blocking.
Reuse a prior explicit decision only when it is documented or clearly approved
for this same project and scope; do not ask again without a new conflict.

## Choose a contract shape

For each approved operation, record its chosen interface type and provide only
the relevant details:

| Concern | API operation                           | Web-route operation                                       |
| ------- | --------------------------------------- | --------------------------------------------------------- |
| Address | Method, path, route version if approved | Method, path, route name if used                          |
| Input   | Path/query/body schema and validation   | Path/query/form input and validation                      |
| Success | Status and JSON schema                  | Page/render target, redirect, or other approved response  |
| Failure | Status and error payload                | Validation presentation, redirect, or approved error page |
| Access  | Authentication mechanism and permission | Session/identity mechanism and permission                 |

Add shared rules for pagination, idempotency, concurrency, rate limits, or
versioning only when required by approved sources. Define field-level
requirements, types, constraints, and source references for every input/output.
Keep error behavior consistent within each confirmed interface type.

## Framework and authentication guardrails

- Do not impose `/api/v1`, JSON envelopes, bearer tokens, or REST conventions
  unless the selected contract mode and approved Tech Spec require them.
- For a Laravel monolith, ordinary browser workflows may use `web` routes with
  the project's existing session, CSRF, controller, redirect, HTML, or Inertia
  conventions. Do not convert them to API routes solely because the artifact is
  called an API Contract.
- Do not add Laravel Sanctum or any token-auth requirement by default. Include
  Sanctum only when the approved Tech Spec, existing architecture, or confirmed
  developer decision requires token-based API authentication. Session-auth API
  or web routes must be described according to the selected project design.
- For other stacks, apply the equivalent principle: use the verified project
  mechanism and version, not framework stereotypes. Do not prescribe
  implementation details absent from the Tech Spec.

## Workflow and output

1. Extract operations from the PRD and relevant Business Flow; map each to a
   screen/action and entity/field source where available.
2. Summarize Tech Spec and existing-route evidence; ask the required interface
   mode question before finalizing routes.
3. After confirmation, define each operation's interface, inputs, success and
   failure behavior, authentication, and authorization by referencing RBAC.
4. Check field names against Data Dictionary, state changes against State
   Machine, and actor access against RBAC. Report mismatches rather than
   silently resolving them.
5. Separate confirmed contract details, recommendations, and open decisions.

Save to `docs/system-design/API_CONTRACT.md` using the project's document
versioning standard. Begin with the confirmed interface mode and evidence.
Organize operations by capability and include traceable request/response or
page/redirect behavior, validation, access rules, errors, and unresolved
decisions. Identify downstream UI and implementation dependencies.
