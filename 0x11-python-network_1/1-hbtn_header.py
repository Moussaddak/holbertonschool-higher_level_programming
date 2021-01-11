#!/usr/bin/python3
""" Get header of the response """
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
        url = argv[1]
        with urlopen(url) as r:
                print(r.headers.get('X-Request-Id'))
