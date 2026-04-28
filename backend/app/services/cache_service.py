import time

CACHE_TTL_SECONDS = 600  # 10 minutes

response_cache = {}
embedding_cache = {}


def get_cache_key(text: str) -> str:
    return text.strip().lower()


def get_cached_response(question: str):
    key = get_cache_key(question)
    item = response_cache.get(key)

    if not item:
        return None

    if time.time() - item["created_at"] > CACHE_TTL_SECONDS:
        del response_cache[key]
        return None

    return item["data"]


def set_cached_response(question: str, data):
    key = get_cache_key(question)
    response_cache[key] = {
        "data": data,
        "created_at": time.time()
    }


def get_cached_embedding(text: str):
    key = get_cache_key(text)
    return embedding_cache.get(key)


def set_cached_embedding(text: str, embedding):
    key = get_cache_key(text)
    embedding_cache[key] = embedding