from sentence_transformers import SentenceTransformer

def load_embedding_model():
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def get_embeddings(model, texts):
    return model.encode(texts, convert_to_tensor=False)