#!/usr/bin/python3
""" Module to read a file """


def read_file(filename=""):
    """ Function to read a file """
    with open(filename, encoding="utf-8") as f:
        return f.read()
