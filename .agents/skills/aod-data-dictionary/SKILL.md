---
name: aod-data-dictionary
description: >-
  Defines traceable domain entities, fields, relationships, constraints, and
  persistence guidance from approved product requirements. Use for a Data
  Dictionary, kamus data, entity definition, or database schema planning.
  Requires PRD as the primary source; use Business Flow, Tech Spec, and existing
  schema when available. Produces docs/business/DATA_DICTIONARY.md.
---

# AOD Data Dictionary

Create the authoritative business-level definition of persisted data. Follow
`.agents/rules/aod-core.md`. The dictionary describes approved domain data; it
does not independently approve product scope or dictate a database engine.

## Sources and boundaries

- Use the approved PRD for entities, capabilities, and required data.
- Use Business Flow and State Machine for lifecycle, ownership, and data
  movement.
- For an existing project, inspect the current schema and record observed
  implementation separately from proposed changes.
- Use Tech Spec for the selected database and supported storage conventions.
- Do not add fields, enum values, relationships, retention rules, or sensitive
  data collection without source evidence. Mark unresolved items as decisions.
- Distinguish persisted fields from derived values, transient request fields,
  external references, and audit metadata.

## Define each entity

Use one table per entity with these columns:

| Field | Logical type | Required/nullability | Default | Constraints | Meaning/source | Sensitivity | Index rationale |
| ----- | ------------ | -------------------- | ------- | ----------- | -------------- | ----------- | --------------- |

For each entity, also state its purpose, identity/primary key, relationships and
cardinality, uniqueness rules, lifecycle/status source, and relevant retention
or deletion behavior when approved. Describe indexes only when query or
integrity needs support them. Add database-specific types, lengths, generated
columns, or engine syntax only when the Tech Spec or existing schema establishes
the target.

## Workflow

1. Extract candidate entities and attributes from approved requirements.
2. Trace each item to its source section or requirement ID; flag untraceable
   items rather than silently including them.
3. Reconcile names and meanings across PRD, Business Flow, State Machine, and
   existing schema. Surface conflicts for resolution.
4. Normalize relationships and constraints at the logical level. Avoid
   duplicate facts and premature physical-schema choices.
   List the approved values and meaning for every enum/status field; defer
   lifecycle transitions to the State Machine.
5. Identify sensitive fields and data-minimization concerns without inventing
   classification or retention policy.
6. Record gaps, assumptions, and decisions separately from approved fields.

## Output

Save to `docs/business/DATA_DICTIONARY.md` using the project's document
versioning standard. Include scope and source references, entity definitions,
relationships, enums, constraints, sensitivity notes, and open decisions. Then
recommend `aod-dbml` when the dictionary is sufficiently approved; DBML must
not add entities or fields absent here.
