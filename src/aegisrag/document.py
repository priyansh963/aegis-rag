from dataclasses import dataclass

@dataclass
class Document:
    content: str
    metadata: dict

@dataclass
class EmbeddedDocument:
    document: Document
    vector : list[float]
