#!/usr/bin/python3
''' A function that divides all elements of a matrix.
'''


def matrix_divided(matrix, div):
    """ Divide a matrix number by number.

    matrix: the matrix to divide.
    div: number to divide the matrix.

    Return: Returns divided matrix.
    """

    new_list = []
    for i in matrix:
        m = []
        if type(i) is not list:
            raise TypeError("matrix must be a matrix\(list of lists) of integers/floats")
        if len(matrix[0]) != len(i):
            raise TypeError('Each row of the matrix must have the same size')
        if type(div) != int and type(div) != float:
            raise TypeError('div must be a number')
        if div == 0:
            raise ZeroDivisionError('division by zero')
        for j in range (len(i)):
            if (type(i[j]) is not int) and (type(i[j]) is not float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            m.append(round(((i[j]) / div), 2))
            new_list.append(m)
        return new_list
