import hashlib
import os
import json

CACHE_FILE = ".client_cache.json"

def hash_code(code):
    return hashlib.sha256(code.encode()).hexdigest()

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f)

def get_cached_result(code):
    cache = load_cache()
    h = hash_code(code)
    return cache.get(h)

def update_cache(code, result):
    cache = load_cache()
    cache[hash_code(code)] = result
    save_cache(cache)
