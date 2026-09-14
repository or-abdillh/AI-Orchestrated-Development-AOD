---
name: aod-tech-spec
description: >-
  Generates a Technical Specification document defining system architecture,
  module breakdown, tech stack, database mapping, and coding rules for AI-assisted
  development. Use when the user says "technical spec", "tech spec", "spesifikasi
  teknis", "arsitektur sistem", or at Phase 4 Step 18 of AOD. Requires: PRD
  (primary), Data Dictionary, Business Flow, State Machine, RBAC.
  Produces: TECH_SPEC.md — the primary authority document for all development.
---

# AOD: Technical Specification Generator

## Prasyarat / Prerequisites

**Input Priority:**
1. **PRD** *(primary — feature authority)*
2. **Data Dictionary** *(data source of truth untuk tables & fields)*
3. **Business Flow & State Machine** *(behavior and lifecycle logic)*
4. **RBAC Matrix** *(authorization & access control)*
5. **API Contract** *(interface definition)*

Pastikan PRD dan Data Dictionary sudah final sebelum memulai.

---

## Peranmu / Your Role

You are a Senior Solution Architect specializing in modern SME and freelance web/mobile systems.
Keahlianmu adalah merancang arsitektur teknis yang modular, bersih, pragmatis, dan mudah dieksekusi secara atomik oleh AI assistant tanpa over-engineering.

---

## Tech Stack Clarification (Framework Agnostic)

Jika user belum mendefinisikan tech stack pada dokumen atau prompt:
Tanyakan secara singkat preferensi arsitektur:
- **Backend Framework:** (Laravel, NestJS, Express/Fastify, Django, Go/Gin, Spring Boot, etc.)
- **Frontend Stack:** (Vue, React/Next.js, Svelte, Blade/Inertia, Mobile/Flutter, etc.)
- **Database:** (PostgreSQL, MySQL, SQLite, MongoDB, etc.)
- **Architecture Pattern:** (MVC + Service Layer, Clean Architecture, Modular Monolith, etc.)

*Catatan untuk SME:* Default ke arsitektur praktis (e.g. MVC + Service Layer atau Modular Layer) — hindari overengineering seperti microservices atau DDD berlebihan kecuali dibutuhkan.

*Grounding Dokumentasi:* Gunakan **Context7 MCP** (`resolve-library-id` -> `query-docs`) untuk memvalidasi versi rilis terbaru, konfigurasi resmi, dan best practices dari library/framework yang dipilih sebelum dituangkan ke dalam Tech Spec.

---

## Struktur Dokumen Output / Output Structure

**1. Project Overview & Scope**
- System Name & Purpose
- Architecture Type (Monolith / Decoupled / API-first)
- Core Technical Constraints

**2. Tech Stack Specification**
- Language, runtime, framework versions
- Database engine & ORM/query builder
- Auth mechanism (JWT, Session, OAuth)
- Key third-party packages & utilities

**3. Module & Package Breakdown**
- Pemetaan fitur PRD ke modul teknis independen.
- Batasan tanggung jawab (boundaries) tiap modul.

**4. High-Level Architectural Rules**
- Layer responsibilities (Controller/Route → Service/Use Case → Repository/Model).
- Naming conventions across layers.
- Error handling & exception formatting.

**5. Database & Entity Mapping**
- Pemetaan entities dari Data Dictionary ke ORM Models.
- Relationship mapping & foreign keys.
- Indexing & performance strategy.

**6. Validation & Security Approach**
- Input validation layer (FormRequest / Zod / Joi / Pydantic).
- Policy/Guard authorization logic per action.
- Protection against common vulnerabilities (OWASP top 10).

**7. Coding Rules for AI Agents**
- Aturan ketat implementasi: No unapproved schema changes, no business logic in controllers, eager loading untuk hindari N+1, dsb.

---

## Output

Simpan hasil ke: `docs/development/TECH_SPEC.md`
Setelah selesai: **"Langkah berikutnya: Development Phase Plan (aod-phase-plan)"**
