#!/usr/bin/env python3
""" FIFO Cache module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Defines a caching system using FIFO eviction policy """
    def __init__(self):
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_order.pop(0)
                else:
                    discarded_key = self.cache_order[0]
                    del self.cache_data[discarded_key]
                    print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            if key not in self.cache_order:
                self.cache_order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
