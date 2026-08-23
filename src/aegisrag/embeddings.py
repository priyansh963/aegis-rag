from dataclasses import dataclass
from aegisrag.document import Document
from sentence_transformers import SentenceTransformer


@dataclass
class EmbeddedDocument:
    document: Document
    vector : list[float]


class Embedder:

    def __init__(self, model_name : str):

        self.model = SentenceTransformer(model_name)

    def embed(self, documents: list[Document]) -> list[EmbeddedDocument]:

        document_content = [document.content for document in documents]

        initial_vectors = self.model.encode(document_content)
        vectors = initial_vectors.tolist()

        embedded_documents = []

        for vector, document in zip(vectors, documents):

            embedded_document = EmbeddedDocument(document = document, vector = vector)

            embedded_documents.append(embedded_document)

        return embedded_documents


    