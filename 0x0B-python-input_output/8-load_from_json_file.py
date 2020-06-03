#!/usr/bin/python3
""" Method """
import json


def load_from_json_file(filename):

    """ creates an Object from a JSON file """

    with open(filename) as file:
        return json.load(file)
