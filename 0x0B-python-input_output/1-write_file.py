#!/usr/bin/python3
""" A function that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """ Writes in filename """
    with open(filename, mode='w', encoding='utf-8') as f:
        num_char = f.write(text)
    return num_char
