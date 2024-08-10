#!/usr/bin/env python3
"""A module with tools for request caching and tracking.
"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis(host='localhost', port=6379, db=0)
'''The module-level Redis instance.
'''


def data_cacher(method: Callable) -> Callable:
    '''Caches the output of fetched data.
    '''
    @wraps(method)
    def invoker(url: str) -> str:
        '''The wrapper function for caching the output.
        '''
        redis_store.incr(f'count:{url}')
        result = redis_store.get(f'result:{url}')
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return invoker


@data_cacher
def get_page(url: str) -> str:
    '''Returns the content of a URL after caching the request's response,
    and tracking the request.
    '''
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return response.text
    except requests.RequestException as e:
        return str(e)

# Example usage:
if __name__ == "__main__":
    print(get_page('http://slowwly.robertomurray.co.uk'))
    print(get_page('http://slowwly.robertomurray.co.uk'))
    print(f"Request count: {redis_store.get('count:http://slowwly.robertomurray.co.uk').decode('utf-8')}")