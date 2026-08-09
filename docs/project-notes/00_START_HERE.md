# AegisRAG — START HERE

> **Purpose:** This file is the handoff/context file for any new ChatGPT conversation.
> If this folder is uploaded to a new chat, read this file first, then read the other Markdown files as needed.

## 1. What is AegisRAG?

**AegisRAG** is the working name of our practical RAG project.

**Repository name:** `aegis-rag`

**Project title:** Enterprise Knowledge & Incident Intelligence Platform

### One-sentence definition

AegisRAG is an AI engineering knowledge and incident-investigation system that retrieves evidence from heterogeneous organizational knowledge and produces evidence-backed answers.

It is intentionally more ambitious than a generic "chat with PDFs" application.

---

## 2. Why are we building it?

There are two goals:

### Learning goal
Learn RAG deeply by building, breaking, debugging, improving, and evaluating a real system.

### Portfolio goal
Create a substantial GitHub project that demonstrates practical AI/RAG engineering rather than a tutorial clone.

The final project should let us discuss:
- retrieval architecture
- chunking
- embeddings
- vector databases
- hybrid retrieval
- reranking
- multi-hop retrieval
- GraphRAG
- agentic RAG
- evaluation
- production trade-offs

We will **only claim capabilities that we actually implement and test**.

---

## 3. How we are learning

For every important concept, use this progression:

**Concept → Why → How → Implement → Break → Debug → Improve → Measure → Interview**

Do not add an advanced RAG technique merely because it sounds impressive.

Each new technique should solve a problem discovered in the previous version.

---

## 4. Current project status

**Current stage:** V1 — basic retrieval foundation

### Completed decisions
- Project named AegisRAG.
- GitHub repo planned as `aegis-rag`.
- Application chosen: Enterprise Knowledge & Incident Intelligence Platform.
- Project will be built progressively.
- Initial implementation will expose RAG mechanics before heavy framework abstraction.
- Initial knowledge base will be a small synthetic engineering organization.
- Project notes will remain Markdown for now.
- A real Obsidian vault will be created later, after the project has matured.

### Current technical target

Build:

```text
Markdown files
    ↓
Load
    ↓
Document objects
    ↓
Chunking
    ↓
Embeddings
    ↓
Similarity retrieval
    ↓
Top-K relevant chunks
```

Then add:

```text
Retrieved chunks
    ↓
Context
    ↓
LLM
    ↓
Grounded answer
```

### Initial knowledge base

Fictional company: **Aurelius Systems**

Initial documents:
- `authentication.md`
- `payments.md`
- `database.md`
- `incidents.md`
- `deployment.md`

---

## New product direction: Obsidian Vault Support

A new planned feature has been added: **local-first Obsidian Vault integration**.

The long-term goal is for a developer to point AegisRAG at their Obsidian vault and ask questions over their own notes.

The system should eventually understand not only Markdown text but also useful Obsidian structure such as:
- `[[wikilinks]]`
- tags
- headings
- frontmatter
- note paths
- backlinks/relationships

Example future flow:

```text
Obsidian Vault
      ↓
Vault scanner
      ↓
Obsidian-aware parser
      ↓
Normalized documents + metadata
      ↓
Vector retrieval + optional graph retrieval
      ↓
Evidence-backed answer
```

Privacy goal: keep the vault local by default and avoid requiring users to upload their private knowledge base to a remote service.

**Status:** planned. We will first build the basic RAG pipeline, then introduce this as a real ingestion/knowledge-source feature.

## 5. What has NOT been built yet

Do not assume these are implemented just because they are in the roadmap:

- persistent vector database
- LLM generation
- citations
- hybrid retrieval
- BM25
- reranking
- evaluation framework
- multi-hop retrieval
- GraphRAG
- CRAG
- Self-RAG
- Agentic RAG
- multimodal RAG
- SQL/structured-data routing
- production deployment

These are future stages.

---

## 6. Planned evolution

```text
V1  Basic / Naive RAG
 ↓
V2  Better ingestion + chunking + metadata
 ↓
V3  Hybrid retrieval
 ↓
V4  Reranking
 ↓
V5  Evaluation
 ↓
V6  Multi-document / multi-hop retrieval
 ↓
V7  GraphRAG
 ↓
V8  CRAG / Self-RAG concepts
 ↓
V9  Agentic RAG
 ↓
V10 Productionization
```

This is a roadmap, **not a promise that every stage will be implemented**. We will decide based on what we learn and what the project actually needs.

---

## 7. Intended use cases

Example questions AegisRAG should eventually answer:

- Why did the authentication service go down?
- Which deployment introduced the problem?
- Who approved the change?
- Which services depend on PostgreSQL?
- What changed between two releases?
- Have we experienced a similar incident before?
- What was the root cause?
- What fixed the incident?
- What preventive action was proposed?

The system should provide evidence/sources where appropriate and should be able to recognize when the available knowledge is insufficient.

---

## 8. Future knowledge sources

We will expand the knowledge base when a technical problem requires it.

Potential sources:
- Markdown
- PDFs
- CSV / JSON
- GitHub repositories
- issues/tickets
- deployment records
- meeting transcripts
- API documentation
- architecture diagrams
- SQL/structured data

Examples:

```text
Exact IDs / logs
    → sparse or hybrid retrieval

Entity relationships
    → graph retrieval

Structured numerical questions
    → SQL / structured retrieval

Architecture diagrams
    → multimodal retrieval

Cross-document questions
    → multi-hop retrieval
```

---

## 9. Documentation rules

The Markdown folder is the project's temporary source of truth.

When a significant project decision is made:
→ update `01_Decisions.md`

When an experiment is performed:
→ update `05_Experiments.md`

When a bug, misconception, or important lesson occurs:
→ update `06_Problems_and_Lessons.md`

When architecture changes:
→ update `02_Architecture.md`

When the knowledge base changes:
→ update `03_Knowledge_Base.md`

When the roadmap changes:
→ update `04_RAG_Learning_Roadmap.md`

When an interview-worthy insight appears:
→ update `07_Interview_Questions.md`

When a capability is genuinely implemented:
→ update `08_Resume_and_GitHub.md`

When something important happens chronologically:
→ update `09_Project_Log.md`

At the end of a working session, update this file's **Current project status** and **Next action**.

---

## 10. How a new chat should behave

If this folder is uploaded to a new chat, the assistant should:

1. Read `00_START_HERE.md` first.
2. Treat the other Markdown files as project context.
3. Preserve existing decisions unless the user explicitly changes them.
4. Never assume future roadmap items have already been implemented.
5. Continue from the current project stage.
6. Check `01_Decisions.md` before proposing a conflicting architecture.
7. Check `09_Project_Log.md` to understand the latest progress.
8. Use `05_Experiments.md` and `06_Problems_and_Lessons.md` to avoid repeating past mistakes.
9. Update the appropriate Markdown files after meaningful decisions or milestones.
10. If the user provides newer information in the conversation, the current conversation takes precedence over older notes.

---

## 11. Important working style

The user wants a practical, skeptical, engineering-oriented learning process.

Do not:
- blindly follow tutorials
- hide important mechanics behind frameworks
- call something "production-ready" without evidence
- claim an architecture is better without measurement
- add complexity without a reason

Do:
- explain why a component exists
- implement it
- inspect intermediate outputs
- intentionally create failure cases
- debug systematically
- benchmark alternatives
- connect implementation to interview questions
- distinguish facts, assumptions, experiments, and decisions

---

## 12. Current next action

**Continue V1 implementation.**

The immediate target is:

```text
Load Markdown
    ↓
Chunk
    ↓
Embed with Sentence Transformers
    ↓
Embed user query
    ↓
Semantic similarity
    ↓
Top-K chunks
```

After this works reliably:

**Next milestone = persistent vector storage + a proper VectorStore abstraction.**

Do not jump to GraphRAG, agents, or other advanced architectures yet.

---

## 13. Source/context note

The user is also following a RAG YouTube course/video. The course transcript is being used as the initial conceptual base, while the AegisRAG project expands beyond it through practical implementation and research when needed.

The project notes should record what we actually decide and build; they should not pretend the video covered material it did not cover.

---

## 14. File map

| File | Purpose |
|---|---|
| `00_START_HERE.md` | New-chat handoff and complete current context |
| `00_Project_Overview.md` | Stable project description and learning philosophy |
| `01_Decisions.md` | Architecture/product/project decisions |
| `02_Architecture.md` | Current and planned architecture |
| `03_Knowledge_Base.md` | Data sources and knowledge-base design |
| `04_RAG_Learning_Roadmap.md` | Learning and implementation roadmap |
| `05_Experiments.md` | Experiments, metrics, conclusions |
| `06_Problems_and_Lessons.md` | Bugs, misconceptions, fixes, lessons |
| `07_Interview_Questions.md` | Interview questions and answers to develop |
| `08_Resume_and_GitHub.md` | Resume/GitHub positioning based on actual implementation |
| `09_Project_Log.md` | Chronological project history |

---

## 15. Last updated

**2026-08-10**

This handoff file should be updated whenever the current project state changes materially.
