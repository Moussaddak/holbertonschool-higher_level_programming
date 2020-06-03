#!/usr/bin/python3
""" Method """
number_of_lines = __import__('1-number_of_lines').number_of_lines


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file (UTF8)
        and prints it to stdout """
    line_number = number_of_lines(filename)
    if 0 >= nb_lines or nb_lines >= line_number:
        nb_lines = line_number
    with open(filename, encoding='utf-8') as file:
        for i in range(nb_lines):
            line = next(file)
            print(line, end='')
