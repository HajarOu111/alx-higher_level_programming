#!/usr/bin/python3
""" This function appends a string at the end of a text file (UTF8)
and returns the number of characters added.
"""

def append_write(filename="", text=""):
    """ Appends a string to a text file """
    with open(filename, mode='a', encoding='utf-8') as f:
        new_file = f.write(text)
    return new_file
