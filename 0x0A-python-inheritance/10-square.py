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
