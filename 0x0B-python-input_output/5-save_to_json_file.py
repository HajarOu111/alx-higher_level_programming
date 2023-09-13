#!/usr/bin/python3
""" This function writes an Object to a text file, using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """ Returns an Object to a text file, using a JSON representation """
    import json
    with open(filename, mode='w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
