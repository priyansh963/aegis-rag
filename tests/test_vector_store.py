from aegisrag.vector_store import VectorStore
from aegisrag.document import Document, EmbeddedDocument
import numpy as np



def test_vector_store_store_and_search():
    doc_a = Document(content="Document A", metadata={"id": "A"})
    embedded_a = EmbeddedDocument(document=doc_a, vector=[1, 0, 0])

    doc_b = Document(content="Document B", metadata={"id": "B"})
    embedded_b = EmbeddedDocument(document=doc_b, vector=[0, 1, 0])

    doc_c = Document(content="Document C", metadata={"id": "C"})
    embedded_c = EmbeddedDocument(document=doc_c, vector=[0.5, 0.5, 0])

    vector_store = VectorStore()

    vector_store.store([embedded_a, embedded_b, embedded_c])

    query_vector = [1, 0, 0]

    results = vector_store.search(query_vector, 3)

    assert results[0][0] == embedded_a
    assert results[1][0] == embedded_c
    assert results[2][0] == embedded_b
