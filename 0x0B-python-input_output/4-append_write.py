#!/usr/bin/python3
""" Method """


def append_write(filename="", text=""):
    """ appends a string at the end of
        a text file (UTF8) and returns the
        number of characters added: """
    with open(filename, mode='a', encoding='utf-8') as file:
        nb_char = file.write(text)
        return nb_char
