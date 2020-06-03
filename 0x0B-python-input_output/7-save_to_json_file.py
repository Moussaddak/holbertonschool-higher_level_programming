#!/usr/bin/python3
""" Method """
import json


def save_to_json_file(my_obj, filename):

    """ writes an Object to a text file,
        using a JSON encoding """
    with open(filename, mode='w') as file:
        file.write(json.dumps(my_obj))
