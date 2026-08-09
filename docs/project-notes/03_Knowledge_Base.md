# Knowledge Base

## Initial fictional organization

**Aurelius Systems**

We use a fictional engineering organization so that the data is controlled, reproducible, and suitable for experiments.

## Initial domains
- Authentication
- Payments
- Infrastructure / Database
- Incidents
- Deployments

## Initial files
- `authentication.md`
- `payments.md`
- `database.md`
- `incidents.md`
- `deployment.md`

## Future data sources
Potential sources, to be introduced when useful:
- PDFs
- Markdown
- CSV / JSON
- GitHub repositories
- issues/tickets
- deployment records
- meeting transcripts
- API documentation
- architecture diagrams
- structured SQL data

## Data design principle
We will intentionally introduce realistic retrieval challenges later:
- duplicate information
- outdated versions
- conflicting information
- irrelevant information
- missing information
- exact identifiers
- cross-document relationships

## Status
The initial five Markdown documents are the current controlled dataset. New sources should be recorded here when introduced.

## Future first-class source: Obsidian

AegisRAG will eventually support an Obsidian vault as a knowledge source.

An Obsidian vault is primarily a collection of Markdown files, but useful structure also exists in:
- folder paths
- headings
- YAML frontmatter
- tags
- `[[wikilinks]]`
- backlinks

The ingestion pipeline should preserve this information rather than flattening everything into plain text.

Example future source:

```text
My Vault/
├── Projects/
├── Architecture/
├── Learning/
├── Notes/
└── Daily/
```

The user should be able to point AegisRAG at a vault directory and ask questions such as:
- "What did I write about hybrid retrieval?"
- "How are these two concepts connected?"
- "Find my notes about vector databases."
- "What have I learned about RAG so far?"
- "Which notes are related to this project?"

This feature should be developed after the basic RAG pipeline works.

