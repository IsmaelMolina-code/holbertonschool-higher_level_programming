#!/usr/bin/python3
""" How to create a class that finds the area of a Square"""


class Square:
    """ Creating the class Square with the private size attribute """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        area = self.__size * self.__size
        return area
