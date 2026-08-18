from aegisrag.document import Document
from aegisrag.chunking import FixedSizeChunker
from pathlib import Path
from aegisrag.ingestion import MarkdownLoader
from aegisrag.chunking import OverlappingChunker

# document = Document(content = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 
#                     metadata = {
#                         "source": "test.md",
#                         "title": "test",
#                         "file_type": "markdown"})

# chunker = FixedSizeChunker(chunk_size = 5)

# chunks = chunker.chunk(document)

# print(f'Number of chunks created {len(chunks)}')

# for chunk in chunks:
#     print(chunk)

"******************************************************************************"

# loader = MarkdownLoader()

# document = loader.load_file(Path("data/documents/incidents.md"))

# chunker = FixedSizeChunker(chunk_size = 200)

# chunks = chunker.chunk(document)

# print(f'Number of chunks created {len(chunks)}')
# print(f'Original document size: {len(document.content)}')

# for chunk in chunks:
#     print("\n" + "=" * 60)
#     print(f"CHUNK {chunk.metadata['chunk_id']}")
#     print("=" * 60)
#     print(chunk.content)

"******************************************************************************"

from aegisrag.chunking import MarkdownChunker


# def test_split_paragraphs():

#     section = {
#         "level": 2,
#         "title": "Root Cause",
#         "content": """The deployment introduced an incompatible database configuration.

#                 This caused the authentication service to lose its PostgreSQL connections.

#                 The service therefore couldn't authenticate users."""
#             }

#     body = section["content"]
#     paragraphs = body.split("\n\n")

#     for paragraph in paragraphs:
#         print("PARAGRAPH:")
#         print(repr(paragraph))
#         print("Length:", len(paragraph))

def test_paragraph_packing():

    section = {
        "level": 2,
        "title": "Root Cause",
        "content": """The deployment introduced an issue.

The database service failed.

This caused the authentication service to lose its connections.

The service therefore couldn't authenticate users."""
}
    body = section["content"]
    paragraphs = body.split("\n\n")

    available_max_chunk_size = 85

    current_chunk = ""
    last_paragraph = None

    for paragraph in paragraphs:

        if not current_chunk:
            current_chunk = paragraph
            last_paragraph = paragraph

        else:
            candidate = current_chunk + "\n\n" + paragraph

            if len(candidate) <= available_max_chunk_size:
                current_chunk = candidate
                last_paragraph = paragraph

            else:
                print("CURRENT CHUNK:")
                print(repr(current_chunk))

                print("LAST PARAGRAPH:")
                print(repr(last_paragraph))

                print("NEXT PARAGRAPH:")
                print(repr(paragraph))

                current_chunk = paragraph
                last_paragraph = paragraph


# loader = MarkdownLoader()

# document = loader.load_file(Path("data/documents/incidents.md"))

# chunker = OverlappingChunker(chunk_size = 200, overlap = 50)

# chunks = chunker.chunk(document)

# print(f'Number of chunks created {len(chunks)}')
# print(f'Original document size: {len(document.content)}')

# for chunk in chunks:
#     print("\n" + "=" * 60)
#     print(f"CHUNK {chunk.metadata['chunk_id']}")
#     print("=" * 60)
#     print(chunk.content)