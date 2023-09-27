#!/usr/bin/python3
""" A subclass that inherites from BaseGeometry. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Constructor of the class """

    def __init__(self, width, height):
        """ The constructor of the superclass
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ if area is implemented """
        return self.__width * self.__height
        
    def __str__(self):
        """ returns the string """
        string = "[" + (str(self.__class__.__name__)) + "] " 
        string += str(self.__width) + "/" + str(self.__height)
        return string
