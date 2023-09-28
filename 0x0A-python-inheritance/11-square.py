#!/usr/bin/python3
""" This class inherites from Rectangle class. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The subclass named Square """

    def __init__(self, size):
        """ Initialization of the subclass
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns the print() and str() representation of a Rectangle"""
        string = "[" + (str(self.__class__.__name__)) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
