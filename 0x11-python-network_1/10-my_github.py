#!/usr/bin/python3
""" My Github! """
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get("id"))
