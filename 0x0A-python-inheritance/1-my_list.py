#!/usr/bin/python3
""" This class inherits from list """


class MyList(list):
    """ Constructor of this subclass """
    def ___init__(self):
        super().__init__(self)

    def print_sorted(self):
        """ Public instance method that  prints the list, but sorted """
        print(sorted(self))
