#!/usr/bin/env python3

import requests
import time
from functools import wraps

CACHE = {}

def track_access_count(func):
    @wraps(func)
    def wrapper(url):
        count_key = f"count:{url}"
        if count_key in CACHE:
            CACHE[count_key] += 1
        else:
            CACHE[count_key] = 1
        return func(url)
    return wrapper

def cache_result(func):
    @wraps(func)
    def wrapper(url):
        if url in CACHE and time.time() - CACHE[url]['timestamp'] < 10:
            return CACHE[url]['content']
        else:
            content = func(url)
            CACHE[url] = {'content': content, 'timestamp': time.time()}
            return content
    return wrapper

@track_access_count
@cache_result
def get_page(url):
    response = requests.get(url)
    return response.text

# Exemple d'utilisation
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/10000/url/http://www.example.com"
    print(get_page(url))
    print(get_page(url))
    print(get_page(url))
    print(f"Nombre d'accès pour {url}: {CACHE.get('count:' + url, 0)}")
