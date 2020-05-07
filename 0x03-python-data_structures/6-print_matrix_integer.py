#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    x = 0
    while x < len(matrix):
        for i in matrix[x]:
            if i != matrix[x][-1]:
                print("{}".format(i), end=" ")
            elif i == matrix[len(matrix) - 1][-1]:
                print("{}".format(i), end='')
            else:
                print("{}".format(i), end="\n");
        x += 1
    print("")
