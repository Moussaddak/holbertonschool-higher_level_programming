#!/usr/bin/python3
""" POST an email #1 """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    info = {'email': argv[2]}
    r = requests.post(url, data=info)
    print(r.text)
