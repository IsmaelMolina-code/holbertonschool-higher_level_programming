#!/usr/bin/python3
""" Creating the class Rectangle """


class Rectangle:
    """ Creating the class Rectangle """

    number_of_instances = 0
    print_symbol = "#"

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
        """ Creating the method height """
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
        Rectangle.number_of_instances += 1

    def area(self):
        """ Creating the method area """
        area = self.__height * self.__width
        return area

    def perimeter(self):
        """ Creating the method perimeter """
        perimeter = self.__height * 2 + self.__width * 2
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        """ Creating the method __str__ """
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = ""
        for h in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width + "\n"
        return rectangle.rstrip()

    def __repr__(self):
        """ Creating the method __repr__ """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Creating the method __del__ """
        print("Bye rectangle...")
        del self
        Rectangle.number_of_instances -= 1
        return

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Creating the method bigger_or_equal """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Creating the method square """
        return cls(size, size)
