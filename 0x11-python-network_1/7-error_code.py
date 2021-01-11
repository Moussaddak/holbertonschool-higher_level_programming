#!/usr/bin/python3
""" Error code #1 """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
        return
    print(r.text)
