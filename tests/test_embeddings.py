from aegisrag.pipeline import run_pipeline
from aegisrag.embeddings import Embedder
from pathlib import Path


def test_embedder_produces_correct_shape():
    chunks = run_pipeline(Path("data/documents/test_comprehensive.md"), max_chunk_size=150, overlap=20)
    embedder = Embedder("all-MiniLM-L6-v2")
    embedded = embedder.embed(chunks)

    assert len(embedded) == len(chunks)
    assert isinstance(embedded[0].vector, list)
    assert len(embedded[0].vector) == 384
