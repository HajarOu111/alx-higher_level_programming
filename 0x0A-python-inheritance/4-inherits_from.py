#!/usr/bin/python3
""" Checks if object is an instance of a class """


def inherits_from(obj, a_class):
    """ Returns: True if the object is an
    instance of the class """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
