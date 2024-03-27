#!/usr/bin/env python3
"""
web.py
"""
import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()


def track_access(method: Callable) -> Callable:
    """Decorator to track the number of times a URL is accessed."""
    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function to track URL access count."""
        redis_store.incr(f"count:{url}")  # Increment the count for the URL
        return method(url)
    return wrapper


def cache_result(method: Callable) -> Callable:
    """Decorator to cache the result of a function."""
    @wraps(method)
    def wrapper(url: str) -> str:
        """Wrapper function to cache the result of the method."""
        key = f"result:{url}"
        cached_result = redis_store.get(key)
        if cached_result:
            return cached_result.decode('utf-8')
        else:
            result = method(url)  # Call the original method
            redis_store.setex(key, 10, result)
            return result
    return wrapper


@cache_result
@track_access
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL and returns it.

    Args:
        url (str): The URL to fetch HTML content from.

    Returns:
        str: The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
