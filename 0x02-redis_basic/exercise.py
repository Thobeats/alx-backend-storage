#!/usr/bin/env python3
""" A module that caches data"""
import redis
from typing import Union
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
