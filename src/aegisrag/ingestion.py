from pathlib import Path
from src.aegisrag.document import Document

class MarkdownLoader:

    def load_file(self, file_path : Path) -> Document:
        content = file_path.read_text(encoding="utf-8")

        metadata = {
            "source": str(file_path),
            "title": self._extract_title(content, file_path),
            "file_type": "markdown"
        }

        return Document(content = content, 
                        metadata = metadata,)
    def load_directory(self, directory : Path) -> list[Document]:
        documents = []
        for file in directory.glob("**/*.md"):
            doc = self.load_file(file)
            documents.append(doc)

        return documents


    def _extract_title(self, content : str, file_path : Path) -> str | None:
        for line in content.splitlines():
            line = line.strip()

            if line.startswith("#"):
                return line[2:].strip()
            
        return file_path.stem