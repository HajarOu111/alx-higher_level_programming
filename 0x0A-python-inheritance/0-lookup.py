#!/usr/bin/python3
'''   
      This function  returns the list of available
      attributes and methods of an object.
'''


def lookup(obj):
    ''' Returns a list of all attributes and methods of object. '''
    return dir(obj)
