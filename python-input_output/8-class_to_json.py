#!/usr/bin/python3
""" This module contains the class to_json """


def class_to_json(obj):
    """ Returns the dictionary representation of an object """
    return obj.__dict__
