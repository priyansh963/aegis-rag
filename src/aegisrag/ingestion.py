from pathlib import Path
from aegisrag.document import Document
from aegisrag.markdown import parse_heading

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
            result = parse_heading(line)

            if result is not None:
                level, title = result
                return title

        
        return file_path.stem

# content = "Just some plain text.\nNo headings here."
# print(MarkdownLoader().load_file(Path("data/documents/test_deep_heading.md")))