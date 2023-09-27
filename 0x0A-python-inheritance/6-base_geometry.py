#!/usr/bin/python3
""" A class BaseGeometry. """


class BaseGeometry:
    """ Public instance method """

    def area(self):
        """ if area is not implemented """
        raise Exception('area() is not implemented')
