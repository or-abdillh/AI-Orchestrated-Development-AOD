---
name: aod-rbac
description: >-
  Defines actors, roles, permissions, resource scope, and conditional access from
  approved product and workflow requirements. Use for RBAC, role-permission
  matrices, access control, or hak akses. Requires PRD; use Business Flow,
  State Machine, and existing authorization design when available. Produces
  docs/business/RBAC.md.
---

# AOD Role and Permission Model

Define who may perform which business actions on which resources, and under what
conditions. Follow `.agents/rules/aod-core.md` and apply least privilege.

## Sources and boundaries

- Use approved PRD for actors, features, and intended access; use Business Flow
  to verify who performs each action.
- Use State Machine for status-based guards and Data Dictionary for ownership,
  tenant, or other scope fields when available.
- For existing projects, separate observed roles/policies from approved target
  permissions. Cite code or configuration as evidence; do not mistake an
  implementation detail for a business approval.
- Authentication establishes identity; this document defines authorization.
  Do not assume an auth provider, role enum, middleware, policy class, or
  framework mechanism unless Tech Spec or project evidence selects it.
- Do not invent roles or grant broad access to fill gaps. Label unresolved
  access decisions and their affected operations.

## Define the model

1. List actors and roles with responsibilities and source references. Keep
   human roles distinct from system/service actors.
2. Build a role-by-resource/action matrix. Use explicit actions such as view,
   create, update, delete, approve, export, or administer only when relevant.
   Mark allowed, denied, or conditional; never leave a blank cell ambiguous.
3. Define conditional access precisely: record/tenant ownership, organization
   scope, lifecycle state, assigned vessel/project, or other source-backed
   condition and its enforcement point.
4. Identify public/unauthenticated operations separately from authenticated
   role permissions.
5. Record separation-of-duty constraints, sensitive actions, audit needs, and
   deny-by-default expectations when supported by the requirements.
6. Cross-check each protected Business Flow action and State Machine transition
   against at least one permission rule. Flag actions with no authorized actor
   and roles with no justified capability.

## Output

Save to `docs/business/RBAC.md` using the project's document versioning
standard. Include sources, actor/role definitions, permission matrix, conditional
rules, sensitive operations, conflicts, and open decisions. Describe
implementation implications at a framework-neutral level; leave concrete
middleware and policy mapping to the approved Tech Spec.
