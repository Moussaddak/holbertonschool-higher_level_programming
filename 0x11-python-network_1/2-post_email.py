#!/usr/bin/python3
from urllib.request import urlopen, Request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    info = {'email': argv[2]}
    data = urllib.parse.urlencode(info).encode('ascii')
    req = Request(url, data)
    with urlopen(req) as r:
        print(r.read().decode('utf-8'))
