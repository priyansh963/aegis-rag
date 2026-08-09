# Project Decisions

This file records decisions made during the AegisRAG project.

## D001 — Project name
**Decision:** Use `AegisRAG` as the project name.

**Repository:** `aegis-rag`

**Reason:** The name is broad enough for the project to evolve from basic RAG into advanced retrieval, graph retrieval, agentic RAG, evaluation, and production components.

---

## D002 — Project scope
**Decision:** Build an Enterprise Knowledge & Incident Intelligence Platform.

**Reason:** This gives us a meaningful engineering problem instead of a generic PDF chatbot and allows us to demonstrate real RAG engineering trade-offs.

---

## D003 — Build progressively
**Decision:** Do not build the final architecture upfront.

**Planned progression:**
1. Naive RAG
2. Better ingestion/chunking/metadata
3. Hybrid retrieval
4. Reranking
5. Evaluation
6. Multi-document / multi-hop retrieval
7. GraphRAG
8. CRAG / Self-RAG concepts
9. Agentic RAG
10. Productionization

**Reason:** Each stage should solve a limitation discovered in the previous stage.

---

## D004 — Start without excessive framework abstraction
**Decision:** The first implementation should expose the mechanics of embeddings, similarity search, retrieval, and context before introducing heavy framework abstractions.

**Reason:** The goal is to understand what RAG is actually doing, not merely call framework functions.

---

## D005 — Initial knowledge source
**Decision:** Start with a small, controlled synthetic engineering knowledge base.

**Initial documents:**
- authentication.md
- payments.md
- database.md
- incidents.md
- deployment.md

**Reason:** A controlled dataset makes it easier to understand retrieval and later create reproducible evaluation questions and deliberate failure cases.

---

## D006 — Knowledge sources will expand when needed
**Decision:** Add new data types only when a RAG problem requires them.

Examples:
- exact IDs/logs → sparse/hybrid retrieval
- linked entities → GraphRAG
- deployment tables → SQL/structured retrieval
- architecture diagrams → multimodal RAG
- evaluation → ground-truth question set

**Reason:** The dataset should grow because the engineering problem grows.

---

## D007 — Obsidian workflow
**Decision:** Do not build the actual Obsidian vault yet.

For now, maintain project notes as Markdown files in this folder. Once the system has been built and the architecture/knowledge structure is stable, convert the accumulated notes into a proper Obsidian vault.

**Reason:** Avoid unnecessary complexity during implementation.

---

## D008 — Obsidian vs GitHub
**Decision:**
- GitHub = code, tests, experiments, benchmarks, project documentation.
- Future Obsidian vault = durable personal knowledge, concepts, lessons, and interconnected notes.

**Reason:** Keep learning notes and engineering artifacts distinct until the project is mature.

## Maintenance rule
This is a living decision log. Do not silently rewrite old decisions. If a decision changes, add a new dated decision explaining what changed and why.

---

## D009 — Obsidian Vault Integration
**Decision:** AegisRAG should eventually support connecting to an Obsidian vault as a first-class knowledge source.

**Use case:** Developers often maintain technical notes, architecture decisions, debugging notes, learning material, and project documentation in Obsidian. AegisRAG should be able to ingest those Markdown notes and answer questions using the user's own knowledge base.

**Planned behavior:**
```text
Obsidian Vault
     ↓
Markdown ingestion
     ↓
Metadata / wikilink / tag extraction
     ↓
Chunking
     ↓
Embeddings + searchable index
     ↓
Retrieval
     ↓
Evidence-backed answer
```

**Important design goal:** The system should understand Obsidian-specific structure where useful, including:
- Markdown files
- `[[wikilinks]]`
- tags
- headings
- note paths/folders
- frontmatter
- backlinks/relationships where available

**Security/privacy principle:** A user's vault should remain local by default. The first implementation should avoid requiring users to upload their entire private vault to a remote service.

**Why:** This turns AegisRAG from a demonstration RAG over synthetic company documents into a practical developer knowledge assistant while giving us a meaningful real-world ingestion problem.

**Status:** Planned feature; not implemented yet.

