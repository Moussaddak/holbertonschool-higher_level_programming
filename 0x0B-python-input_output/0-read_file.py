#!/usr/bin/python3
""" Method """


def read_file(filename=""):
    """ function reads a text file encoded UTF8 and prints it"""
    with open(filename, encoding='utf-8') as file:
        print(file.read())
