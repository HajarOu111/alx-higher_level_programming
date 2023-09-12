#!/usr/bin/python3
""" This function reads a text file (UTF8) 
and prints it to stdout
"""


def read_file(filename=""):
    """ Opens the file in read mode """
    with open('my_file_0.txt', 'r') as file:
        for line in file:
            print(line.strip())
