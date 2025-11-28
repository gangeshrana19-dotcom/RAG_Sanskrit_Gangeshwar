from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

class Retriever:
    def __init__(self, chunks):
        self.chunks = chunks
        self.vectorizer = TfidfVectorizer(max_features=20000)
        self.embeddings = self.vectorizer.fit_transform(chunks)

    def search(self, query, top_k=3):
        query_vec = self.vectorizer.transform([query])
        scores = linear_kernel(query_vec, self.embeddings).flatten()
        top_indices = scores.argsort()[-top_k:][::-1]
        return [self.chunks[i] for i in top_indices]
