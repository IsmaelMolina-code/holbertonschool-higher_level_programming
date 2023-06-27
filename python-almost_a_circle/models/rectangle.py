#!/usr/bin/python3
""" Defines a Rectangle class """


from models.base import Base

class Rectangle(Base):
    """ The class """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
