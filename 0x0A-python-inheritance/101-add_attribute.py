#!/usr/bin/python3
""" a function that adds a new attribute to an object if it’s possible """


def add_attribute(obj, attr_name, attr_value):
    """ Checks if the object has an attribute or not
    """
    if not hasattr(obj, '__dict__'):
        raise Exception("can't add new attribute")
    setattr(obj, attr_name, attr_value)
