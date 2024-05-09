#!/usr/bin/env python3
"""LFUCache module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Defines a caching system using LFU eviction policy """
    def __init__(self):
        super().__init__()
        self.frequency = {}
        self.usage_count = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            items_with_min_freq = [k for k, v in self.frequency.items()
                                   if v == min_freq]
            if len(items_with_min_freq) > 1:
                lru_key = min(items_with_min_freq, key=lambda k:
                              self.usage_count.get(k, 0))
                if key not in self.cache_data:
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    del self.usage_count[lru_key]
                    print("DISCARD:", lru_key)
            else:
                key_to_remove = items_with_min_freq[0]
                if key not in self.cache_data:
                    del self.cache_data[key_to_remove]
                    del self.frequency[key_to_remove]
                    del self.usage_count[key_to_remove]
                print("DISCARD:", key_to_remove)

        self.cache_data[key] = item
        self.frequency[key] = 1
        self.usage_count[key] = 0

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_count[key] += 1

        return self.cache_data[key]
