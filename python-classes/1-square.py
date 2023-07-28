#!/usr/bin/python3
""" How to create a class with a private attribute"""


class Square:
    """ Creating the class Square with the private size attribute """
    def __init__(self, size):
        self.__size = size
