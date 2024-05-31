#!/usr/bin/env python3
"""Returns the length of each element in a list"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return length of the element
    """
    return [(i, len(i)) for i in lst]
