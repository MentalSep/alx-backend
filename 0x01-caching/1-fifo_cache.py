#!/usr/bin/env python3
""" FIFO Cache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Defines a caching system using FIFO eviction policy """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                if key not in self.cache_data:
                    del self.cache_data[first_key]
                    print("DISCARD:", first_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
