#!/usr/bin/env python3
"""Module for task 0"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """he start and end index for a given page and page size"""

    start = (page - 1) * page_size
    end = start + page_size

    return start, end
