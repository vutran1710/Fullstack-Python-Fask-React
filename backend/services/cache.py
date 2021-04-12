from typing import Any


class Cache(ABC):
    """A modular cache service
    can be in-memory or remote like Redis or Memcache
    For demonstration purpose of this app,
    we use in-memory caching method
    """

    __store__ = dict()

    def save_data(self, key: str, value: Any):
        self.__store__.update({key: value})

    def get_data(self, key: str):
        return self.__store__.get(key)
