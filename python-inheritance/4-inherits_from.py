#!/usr/bin/python3
""" Function that returns True if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance of a class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
