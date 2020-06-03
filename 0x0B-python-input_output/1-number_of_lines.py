#!/usr/bin/python3
""" Method """


def number_of_lines(filename=""):
    """ function reads a text file encoded UTF8 and prints it"""
    line_number = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            line_number += 1
        return line_number
