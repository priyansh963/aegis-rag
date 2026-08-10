from pathlib import Path

from aegisrag.ingestion import MarkdownLoader


def test_load_file():
    loader = MarkdownLoader()

    document = loader.load_file(Path("data/documents/incidents.md"))

    assert document.metadata["title"] == "Incident INC-2026-1042"
    # assert document.content.startswith("## Incident Metadata")
    assert document.metadata["file_type"] == "markdown"

    assert "Authentication Service" in document.content

def test_load_file_without_heading(tmp_path):
    test_file = tmp_path / "developer_note.md"

    test_file.write_text("This is a test file without a heading.", encoding="utf-8")

    loader = MarkdownLoader()

    document = loader.load_file(test_file)

    assert document.metadata["title"] == "developer_note"
    assert document.content == "This is a test file without a heading."
    assert document.metadata["file_type"] == "markdown"

def test_load_directory():
    loader = MarkdownLoader()

    documents = loader.load_directory(Path("data/documents"))

    titles = {document.metadata["title"] for document in documents}

    assert len(documents) == 5
    assert "Authentication Service" in titles
    assert "Incident INC-2026-1042" in titles
    assert "Payment Service" in titles