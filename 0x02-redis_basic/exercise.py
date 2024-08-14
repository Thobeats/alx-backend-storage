#!/usr/bin/env python3
""" A module that caches data"""
import redis
from typing import Union, Callable, Optional
from uuid import uuid4
import functools


def count_calls(method: Callable) -> Callable:
    """Count the number of times the Cache class was called"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper to count calls"""
        key = method.__qualname__

        self._redis.incr(key)

        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs"""
    key = method.__qualname__
    input_key = "{}:inputs".format(key)
    output_key = "{}:outputs".format(key)

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper to call history"""
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable) -> None:
    """Shows a history of a function"""
    function_name = method.__qualname__
    cache = redis.Redis()
    function_calls = cache.get(function_name).decode('UTF-8')
    print("{} was called {} times".format(function_name, function_calls))
    inputs = cache.lrange(function_name + ":inputs", 0, -1)
    outputs = cache.lrange(function_name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(function_name, i.decode('utf-8'),
                                     o.decode('utf-8')))


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

    @count_calls
    @call_history
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
