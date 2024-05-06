#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary with hypermedia pagination information
        based on the provided index"""

        assert index is None or 0 <= index < len(self.indexed_dataset())

        Set = self.indexed_dataset()
        next_index = index + page_size
        data = [Set.get(i) for i in range(index, min(next_index, len(Set)))]
        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index if next_index < len(Set) else None
        }
