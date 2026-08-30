from aegisrag.ingestion import MarkdownLoader
from aegisrag.markdown import parse_sections
from aegisrag.chunking import MarkdownChunker
from pathlib import Path
from aegisrag.embeddings import Embedder
from aegisrag.vector_store import VectorStore


def run_pipeline(file_path : Path, max_chunk_size : int, overlap : int, model_name : str):
    loader = MarkdownLoader()

    document = loader.load_file(file_path)

    sections = parse_sections(document.content)

    chunker = MarkdownChunker(max_chunk_size = max_chunk_size, overlap = overlap)

    chunks = chunker.chunk(document, sections)

    embedder = Embedder(model_name)

    embedded_documents = embedder.embed(chunks)

    vector_store = VectorStore()

    vector_store.store(embedded_documents)

    return vector_store


if __name__ == "__main__":

    vector_store =run_pipeline(Path("data/documents/test_comprehensive.md"), max_chunk_size=100, overlap=20, model_name="all-MiniLM-L6-v2")

    for ed in vector_store.documents:
        print(ed.document.metadata["chunk_id"], ed.document.metadata["section"], len(ed.vector))

    query_vector = vector_store.documents[0].vector
    results = vector_store.search(query_vector, k=3)
    for doc, score in results:
        print(score, doc.document.metadata["section"])
    

    
