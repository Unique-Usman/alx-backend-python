#!/usr/bin/env python3
"""Return the sum of the element in a list with mix type"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """
    Calculate the sum of a list with mix type
    """
    return sum(mxd_list)
