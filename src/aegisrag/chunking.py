from aegisrag.document import Document

class FixedSizeChunker:

    def __init__(self, chunk_size : int):

        self.chunk_size = chunk_size
        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")

    def chunk(self, document : Document) -> list[Document]:
        
        start = 0

        chunks = []

        while start < len(document.content):

            chunk_content = document.content[start:start + self.chunk_size]
            metadata = document.metadata.copy()
            metadata["chunk_id"] = len(chunks)

            chunks.append(Document(content = chunk_content, metadata = metadata,))

            start += self.chunk_size

        return chunks


class OverlappingChunker:

    def __init__(self, chunk_size : int, overlap : int):


        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")

        if overlap < 0:
            raise ValueError("overlap must be greater than or equal to 0")

        if overlap >= chunk_size:
            raise ValueError("overlap must be less than chunk_size")

        self.chunk_size = chunk_size 
        self.overlap = overlap

    def chunk(self, document : Document) -> list[Document]:

        start = 0

        chunks = []

        while start < len(document.content):

            chunk_content = document.content[start:start + self.chunk_size]
            metadata = document.metadata.copy()
            metadata["chunk_id"] = len(chunks)

            chunks.append(Document(content = chunk_content, metadata = metadata,))

            start += self.chunk_size - self.overlap

        return chunks

class MarkdownChunker:

    def __init__(self, max_chunk_size : int, overlap : int):

        if max_chunk_size <= 0:
            raise ValueError("max_chunk_size must be greater than 0")

        if overlap < 0:
            raise ValueError("overlap must be greater than or equal to 0")

        if overlap >= max_chunk_size:
            raise ValueError("overlap must be less than max_chunk_size")

        self.max_chunk_size = max_chunk_size
        self.overlap = overlap

    def chunk(self, document : Document, sections : list[dict]) -> list[Document]:

        chunks = []

        for section in sections:

            if section["level"] == 0:
                heading_context = ""
                heading_length = 0

            else:

                heading = "#" * section["level"] + " "+ section["title"]

                heading_context = heading + "\n\n"

                heading_length = len(heading_context)

            body = section["content"]

            available_max_chunk_size = self.max_chunk_size - heading_length

            if len(body) <= available_max_chunk_size:

                metadata = document.metadata.copy()
                metadata["chunk_id"] = len(chunks)
                metadata["section"] = section["title"]
                metadata["heading_level"] = section["level"]

                chunks.append(Document(content = heading_context + body, metadata = metadata,))
                continue

            else:

                paragraphs = body.split("\n\n")
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

                        else:

                            chunk_content = heading_context + current_chunk

                            metadata = document.metadata.copy()
                            metadata["chunk_id"] = len(chunks)
                            metadata["section"] = section["title"]
                            metadata["heading_level"] = section["level"]

                            chunks.append(Document(content = chunk_content, metadata = metadata,))

                            current_chunk = paragraph

                if current_chunk:

                    chunk_content = heading_context + current_chunk

                    metadata = document.metadata.copy()
                    metadata["chunk_id"] = len(chunks)
                    metadata["section"] = section["title"]
                    metadata["heading_level"] = section["level"]

                    chunks.append(Document(content = chunk_content, metadata = metadata,))
        return chunks

    def format_section(self, section : dict) -> str:

        level = section["level"]
        title = section["title"]
        content = section["content"]

        if level == 0:
            return content

        heading = "#" * level

        return f"{heading} {title}\n\n{content}"
