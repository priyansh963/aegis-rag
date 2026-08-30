from aegisrag.embeddings import EmbeddedDocument
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


class VectorStore:

    def __init__(self):
        self.documents = []

    def store(self, documents : list[EmbeddedDocument]):

        self.documents.extend(documents)

    def search(self, query_vector : list[float], k : int):

        similarities = []

        for document in self.documents:

            similarity = cosine_similarity(query_vector, document.vector)

            similarities.append((document, similarity))

        sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

        return sorted_similarities[:k]

    