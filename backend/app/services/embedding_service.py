from sentence_transformers import SentenceTransformer
from app.services.cache_service import get_cached_embedding, set_cached_embedding

model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text: str):
    cached_embedding = get_cached_embedding(text)

    if cached_embedding:
        return cached_embedding

    embedding = model.encode(text).tolist()

    set_cached_embedding(text, embedding)

    return embedding