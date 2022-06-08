#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = []
    for y in matrix:
        sqr.append(list(map(lambda y: y**2, y)))
    return (sqr)
