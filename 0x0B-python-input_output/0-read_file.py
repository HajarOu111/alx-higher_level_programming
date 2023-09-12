#!/usr/bin/python3
""" This function reads a text file (UTF8) 
and prints it to stdout
"""


def read_file(filename=""):
    """ Opens the file in read mode """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
