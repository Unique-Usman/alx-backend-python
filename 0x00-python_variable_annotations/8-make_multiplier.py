#!/usr/bin/env python3
"""
Create multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Make a multiplier function
    """

    def multiply(n: float) -> float:
        return multiplier * n
    return multiply
