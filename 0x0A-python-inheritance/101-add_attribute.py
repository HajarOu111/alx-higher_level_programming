#!/usr/bin/python3
"""this module defines a function that adds attributes to an object"""


def add_attribute(obj, att, value):
    """ Adds a new attribute if it's possible
    """
    if not hasattr(obj, "__dict__"):
        raise Exception("can't add new attribute")
    setattr(obj, att, value)
