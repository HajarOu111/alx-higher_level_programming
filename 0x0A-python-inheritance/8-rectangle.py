#!/usr/bin/python3
""" A subclass that inherites from BaseGeometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Constructor of the class """

    def __init__(self, width, height):
        """ The constructor of the superclass
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
