#!/usr/bin/env python3
"""
Implémente un cache web expirant et un suivi
"""
from typing import Callable
from functools import wraps
import redis
import requests

redis_client = redis.Redis()

def url_count(method: Callable) -> Callable:
    """Compte combien de fois une URL est consultée"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        url = args[0]
        redis_client.incr(f"count:{url}")
        cached = redis_client.get(url)
        if cached:
            return cached.decode('utf-8')
        content = method(*args, **kwargs)
        redis_client.setex(url, 10, content)
        return content
    return wrapper

@url_count
def get_page(url: str) -> str:
    """Obtient une page et met en cache la valeur"""
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
