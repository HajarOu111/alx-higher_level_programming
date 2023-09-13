#!/usr/bin/python3
""" This class defines a student. """


class Student:
    """ Initialization of class student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ A function that retrieves a dictionary representation of a Student,
        Retrieves only attribute names contained in this list if attrs is a
        list of strings.
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
