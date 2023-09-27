#!/usr/bin/python3
""" A class BaseGeometry. """


class BaseGeometry:
    """ Public instance method """

    def area(self):
        """ if area is not implemented """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
