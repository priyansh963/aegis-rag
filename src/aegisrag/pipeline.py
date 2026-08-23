from aegisrag.ingestion import MarkdownLoader
from aegisrag.markdown import parse_sections
from aegisrag.chunking import MarkdownChunker
from pathlib import Path
from aegisrag.embeddings import Embedder


def run_pipeline(file_path : Path, max_chunk_size : int, overlap : int, model_name : str):
    loader = MarkdownLoader()

    document = loader.load_file(file_path)

    sections = parse_sections(document.content)

    chunker = MarkdownChunker(max_chunk_size = max_chunk_size, overlap = overlap)

    chunks = chunker.chunk(document, sections)

    embedder = Embedder(model_name)

    embedded_documents = embedder.embed(chunks)

    return embedded_documents

if __name__ == "__main__":

    embedded_documents = run_pipeline(Path("data/documents/test_comprehensive.md"), max_chunk_size=100, overlap=20, model_name="all-MiniLM-L6-v2")

    
    for ed in embedded_documents:
        print(ed.document.metadata["chunk_id"], ed.document.metadata["section"], len(ed.vector))
