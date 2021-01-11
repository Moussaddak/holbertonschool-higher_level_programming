#!/usr/bin/python3
""" Error code #0 """
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as r:
            print(r.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
