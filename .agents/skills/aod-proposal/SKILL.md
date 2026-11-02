---
name: aod-proposal
description: >-
  Creates a client-facing project proposal, scope of work, delivery estimate,
  and quotation from a stable approved PRD and Technical Specification. Use for
  a proposal, SOW, project quotation, or commercial estimate. Use the approved
  Phase Plan, capacity, and rate card when available; disclose missing inputs
  and never invent price rates or commitments. Produces
  docs/proposal/PROPOSAL.md.
---

# AOD Technical-to-Commercial Proposal

Translate approved product scope and technical boundaries into a reviewable
commercial proposal. Follow `.agents/rules/aod-core.md`. A proposal is a draft
for stakeholder review; it does not approve scope, prices, dates, or contract
terms on behalf of the client or developer.

## Readiness and sources

For a client-ready proposal, require the PRD and Tech Spec to be approved and
stable for the same scope. Read the approved Phase Plan when available for
sequencing and delivery milestones. Use other sources only as relevant:

- BRD/Business Flow for outcomes and workflows.
- Data Dictionary, RBAC, State Machine, API Contract, and UI plans for scope
  detail and risk.
- Repository baseline for existing-project work.
- User-provided team capacity, calendar, rate card, currency, tax treatment,
  budget cap, and commercial terms.

If PRD or Tech Spec is missing, draft only a clearly marked preliminary concept
when the user explicitly requests it. Do not present it as a fixed SOW, timeline,
or quotation. If the documents disagree, list the conflicting scope/decision
and pause only affected estimates.

## Estimation rules

1. Build a traceable work breakdown from PRD requirement IDs mapped to Tech Spec
   modules and, when available, Phase Plan items. Include only approved scope;
   list exclusions and dependencies explicitly.
2. Estimate work packages by role and effort unit using known team data,
   historical evidence, or user-provided assumptions. Explain drivers such as
   integrations, data migration, security, offline behavior, deployment, QA,
   UAT, and handover only where relevant. Label confidence and uncertainty per
   package; do not convert vague complexity labels directly into precise hours.
3. Distinguish **effort** (person-hours/days) from **elapsed duration**.
   Derive duration from dependency order, actual capacity, availability, and
   allowed parallelism. Align to the approved Phase Plan where available. Use
   ranges when uncertainty is material; do not invent a kickoff date, sprint
   length, weekly Gantt schedule, or team capacity.
4. Calculate price only from an approved rate card or user-authorized pricing
   basis:
   `labor by role + approved direct costs + explicitly agreed contingency/tax`.
   State currency and inclusions. If rates or tax treatment are unknown, show
   effort and mark price as `TBD`; do not invent market rates. An illustrative
   price range may use only a user-provided provisional rate/budget basis; it
   requires an explicit request, clearly labels every assumption, and must not
   be described as a binding quote.
5. Treat payment milestones, warranty, support, change-request rates, and
   acceptance terms as negotiable inputs. Do not impose a default payment split.
6. Quantify ROI or savings only when supporting baseline and assumptions are
   provided; otherwise describe qualitative value without fabricated metrics.

## Proposal structure

Create a concise, client-readable document containing the sections that apply:

1. **Document Basis** — client/project, source versions/status, date, proposal
   status (`Preliminary`, `Indicative`, or `Ready for Review`), assumptions.
2. **Executive Summary** — approved business problem, intended outcome, and
   value proposition grounded in the PRD/BRD.
3. **Scope of Work** — deliverables mapped to requirement/Phase Plan IDs,
   dependencies, exclusions, and acceptance boundaries.
4. **Technical Approach** — approved Tech Spec choices and constraints, not
   unsolicited architecture claims.
5. **Delivery Plan** — milestones, dependencies, effort, elapsed duration,
   owner/capacity basis, confidence, and open decisions.
6. **Investment** — work-package estimate and calculation basis. Use `TBD` for
   price inputs that are unavailable; separate taxes and third-party costs.
7. **Assumptions, Risks, and Change Control** — source, impact, owner, and
   effect on estimates if changed.
8. **Commercial Terms and Approval** — only provided or explicitly approved
   terms; leave unresolved terms as placeholders for review.

## Output

Save to `docs/proposal/PROPOSAL.md` using the project's document versioning
standard. Add traceability tables from requirement IDs to deliverables and
estimate rows. Separate approved facts, estimation assumptions, and open
commercial decisions. End with the inputs needed to firm up any indicative
scope, schedule, or price; do not claim client approval or contractual status.


## Orchestrator handoff

When invoked by `aod-orchestrator`, read
`.agents/skills/aod-orchestrator/references/handoff.md`, return its structured
handoff, and return control to the orchestrator. Do not write workflow checkpoint.
Direct invocation authorizes only the requested scope, not the full workflow.
