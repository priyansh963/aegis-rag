from aegisrag.retriever import Retriever
from aegisrag.vector_store import VectorStore
from aegisrag.embeddings import Embedder
from aegisrag.document import Document

import numpy as np

def test_retriever_retrieve():

    vector_store = VectorStore()
    embedder = Embedder("all-MiniLM-L6-v2")

    retriever = Retriever(vector_store, embedder)

    doc_a = Document(content="The cat sat quietly on the warm windowsill.", metadata={"id": "A"})
    doc_b = Document(content="Rocket engines burn fuel to generate thrust.", metadata={"id": "B"})
    doc_c = Document(content="The stock market rose sharply today.", metadata={"id": "C"})

    docs = [doc_a, doc_b, doc_c]

    embedded_docs = embedder.embed(docs)

    embedded_a = embedded_docs[0]
    embedded_b = embedded_docs[1]
    embedded_c = embedded_docs[2]

    vector_store.store([embedded_a, embedded_b, embedded_c])

    results = retriever.retrieve("Tell me something about pets", 3)

    assert results[0][0].document.metadata["id"] == "A"
