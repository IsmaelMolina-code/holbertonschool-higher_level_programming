#!/usr/bin/python3
""" Creating the class Rectangle """


class Rectangle:
    """ Creating the class Rectangle """

    @property
    def width(self):
        """ Creating the method width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Creating the method width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ Creating the method height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """ Creating the method __init__ """
        self.height = height
        self.width = width

    def area(self):
        area = self.__height * self.__width
        return area

    def perimeter(self):
        perimeter = self.__height * 2 + self.__width * 2
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        return perimeter
