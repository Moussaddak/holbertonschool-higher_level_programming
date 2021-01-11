#!/usr/bin/python3
""" Response header value #1 """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    data = requests.get(url)
    print(data.headers.get("X-Request-Id"))
