#!/usr/bin/python3
""" a function that adds a new attribute to an object """


def add_attribute(obj, name, value):
    """ Adds a new attribute if it's possible
    """
    if not hasattr(obj, "__dict__"):
        raise Exception("can't add new attribute")
    setattr(obj, name, value)
