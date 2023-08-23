#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) == 0:
        return
    l = reversed(my_list)
    for int in l:
        print("{}".format(int))
