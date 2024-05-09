#!/usr/bin/env python3
"""MRU Cache module"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Defines a caching system using MRU eviction policy """
    def __init__(self):
        super().__init__()
        self.used_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = self.used_order.pop()
                if key not in self.cache_data:
                    del self.cache_data[mru_key]
                    print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.used_order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.used_order.remove(key)
            self.used_order.append(key)
            return self.cache_data[key]
