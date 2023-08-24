#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for h in matrix:
        for i in h:
            print("{:d}".format(i), end='')
            if i != h[-1]:
                print(' ', end='')
        print("")
