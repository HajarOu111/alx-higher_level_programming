#!/usr/bin/python3
""" A class that inherites from int class """


class MyInt(int):
    """ MyInt has == and != operators inverted """

    def equal(self, value):
        """ the equal == behavior """
        return self.real != value

    def not_equal(self, value):
        """ Not equal != behavior """
        return self.real == value
