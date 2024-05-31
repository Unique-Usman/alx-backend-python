#!/usr/bin/env python3
"""
Returns a tuple of string and int or float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple of string and int or float
    """
    return (k, v * v)
