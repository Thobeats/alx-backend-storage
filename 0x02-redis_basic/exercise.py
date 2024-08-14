#!/usr/bin/env python3
""" A module that caches data"""
import redis
from typing import Union, Callable, Optional
from uuid import uuid4


class Cache:
    """Cache Class

    Attributes:
    _redis: Redis Client
    store(): stores the data as cache
    """

    def __init__(self) -> None:
        """initialise the cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store a redis cache"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """Get Data from the Cache"""

        value = self._redis.get(key)
        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """Get a string value from the cache"""
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """Get an int value from the cache"""
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
