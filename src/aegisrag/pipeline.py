from aegisrag.ingestion import MarkdownLoader
from aegisrag.markdown import parse_sections
from aegisrag.chunking import MarkdownChunker
from pathlib import Path


def run_pipeline(file_path : Path, max_chunk_size : int, overlap : int):
    loader = MarkdownLoader()

    document = loader.load_file(file_path)

    sections = parse_sections(document.content)

    chunker = MarkdownChunker(max_chunk_size = max_chunk_size, overlap = overlap)

    chunks = chunker.chunk(document, sections)

    return chunks

chunks = run_pipeline(Path("data/documents/test_comprehensive.md"), max_chunk_size=100, overlap=20)
print(chunks)

# content = Path("data/documents/test_comprehensive.md").read_text()
# print(content.count("```"))