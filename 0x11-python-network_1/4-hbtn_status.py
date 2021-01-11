#!/usr/bin/python3
""" What's my status? #1 """
from urllib.request import urlopen

url = 'https://intranet.hbtn.io/status'
with urlopen(url) as r:
    data = r.read().decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
