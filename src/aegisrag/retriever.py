from aegisrag.document import Document
from aegisrag.vector_store import VectorStore
from aegisrag.embeddings import Embedder

class Retriever:

    def __init__(self, vector_store : VectorStore, embedder : Embedder):
        self.vector_store = vector_store
        self.embedder = embedder

    def retrieve(self, query : str, k : int):

        query_vector = self.embedder.embed([Document(content=query, metadata={})])[0].vector

        return self.vector_store.search(query_vector, k)