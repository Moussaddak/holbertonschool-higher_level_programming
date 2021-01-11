#!/usr/bin/python3
from urllib.request import urlopen
from sys import argv



url = argv[1]
with urlopen(url) as r:
        print(r.headers.get('X-Request-Id'))
