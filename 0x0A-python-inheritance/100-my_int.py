#!/usr/bin/python3
""" A class that inherites from int class """


class MyInt(int):
    """ MyInt has == and != operators inverted """

    def __eq__(self, value):
        """ the equal == behavior """
        return self.real != value

    def __ne__(self, value):
        """ Not equal != behavior """
        return self.real == value
