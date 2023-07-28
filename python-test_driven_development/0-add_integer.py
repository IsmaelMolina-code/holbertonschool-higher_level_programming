#!/usr/bin/python3
"""This module contains a single function that adds two numbers"""

def add_integer(a, b=98):
    """Adds two numbers
    Args:
        a: first number
        b: second number
    Returns:
        The addition of a and b
    Raises:
        TypeError: If either of a or b is a non-integer and non-float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float('inf') or a == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer.")
    return int(a) + int(b)
