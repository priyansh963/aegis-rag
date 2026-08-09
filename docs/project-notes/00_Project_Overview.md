# AegisRAG — Project Overview

## Project name
**AegisRAG**

## Working title
**Enterprise Knowledge & Incident Intelligence Platform**

## Core idea
AegisRAG is an AI engineering knowledge and incident-investigation system. It will answer engineering questions across heterogeneous organizational knowledge and provide evidence-backed answers.

The goal is not to build a generic "chat with PDFs" application. The project will progressively demonstrate and compare different RAG architectures.

## Example questions
- Why did the authentication service go down?
- Which deployment introduced the problem?
- Who approved the change?
- Which services depend on PostgreSQL?
- What changed between two releases?
- Have we experienced a similar incident before?

## Learning philosophy
We will learn RAG practically:
1. Understand a concept.
2. Implement it.
3. Break it intentionally.
4. Debug it.
5. Improve it.
6. Measure it.
7. Connect it to interview/system-design questions.

## Important principle
Architecture should solve a real retrieval/problem constraint. We will not add RAG techniques merely to make the project sound advanced.


## Current state

We are at the beginning of V1. The immediate implementation target is to load the initial Markdown knowledge base, chunk it, create embeddings, embed a query, and perform semantic top-K retrieval.

See `00_START_HERE.md` for the authoritative new-chat handoff.
