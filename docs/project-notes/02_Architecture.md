# Current Architecture

## Current stage: V1

We are starting with the simplest RAG pipeline.

```text
Markdown documents
        ↓
Load
        ↓
Document objects
        ↓
Chunking
        ↓
Embeddings
        ↓
Vector representation
        ↓
Similarity retrieval
        ↓
Top-K chunks
        ↓
Context
        ↓
LLM (next stage)
```

## Current implementation goal

First make this work:

```text
.md files
   ↓
load
   ↓
chunks
   ↓
Sentence Transformer embeddings
   ↓
query embedding
   ↓
cosine/semantic similarity
   ↓
top-k relevant chunks
```

## Planned final architecture

The eventual system may contain:

```text
                    User Query
                        ↓
                  Query Router
                        ↓
        ┌───────────────┼────────────────┐
        ↓               ↓                ↓
   Vector Search       SQL          Graph Search
        │               │                │
        └───────────────┼────────────────┘
                        ↓
                    Reranker
                        ↓
                 Evidence Set
                        ↓
                       LLM
                        ↓
              Grounding / Evaluation
                        ↓
                 Answer + Sources
```

This is a target direction, not a commitment that every component will necessarily be implemented.

## Status rule
Clearly separate **implemented**, **planned**, and **experimental** architecture. A planned component must not be described as implemented.

## Future developer knowledge source

Obsidian should eventually be another ingestion connector:

```text
Obsidian Vault
      ↓
Vault Scanner
      ↓
Markdown + Obsidian Metadata Parser
      ↓
Normalized Documents
      ↓
Chunking / Embeddings
      ↓
Vector Store

Wikilinks / backlinks
      ↓
Entity + relationship extraction
      ↓
Knowledge Graph
```

This is a planned extension, not part of V1.

