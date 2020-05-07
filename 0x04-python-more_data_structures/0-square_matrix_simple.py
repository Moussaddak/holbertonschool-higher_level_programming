#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if matrix:
        new_matrix = []
        for i in range(len(matrix)):
            tmp = []
            for j in matrix[i]:
                tmp.insert(matrix[i].index(j), j ** 2)
            new_matrix.append(tmp)
        return (new_matrix)
