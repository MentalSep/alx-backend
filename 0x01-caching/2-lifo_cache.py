#!/usr/bin/env python3
"""LIFO Cache module"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Defines a caching system using LIFO eviction policy """
    def __init__(self):
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.cache_order.pop()
                if key not in self.cache_data:
                    del self.cache_data[discarded_key]
                    print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            self.cache_order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
