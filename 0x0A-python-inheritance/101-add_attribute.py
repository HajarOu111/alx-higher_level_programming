#!/usr/bin/python3
""" a function that adds a new attribute to an object if it’s possible.
"""

def add_attribute(obj, attr_name, attr_value):
    """ Checks if the object has an attribute or not """

    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise Exception("can't add new attribute")
