#!/usr/bin/python3
""" Prototype to read a file """


def read_file(filename=""):
    """ Function to read a file """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
