#!/usr/bin/python3
""" Write a function that appends a string to a text file (UTF8) """


def append_write(filename="", text=""):

    """ Write a string to a text file (UTF8)  """
    chars = 0
    for chars in range(len(text)):
        chars += 1
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return chars
