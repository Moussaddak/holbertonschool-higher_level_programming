#!/usr/bin/python3
from urllib.request import urlopen

url = 'https://intranet.hbtn.io/status'
with urlopen(url) as r:
    data = r.read()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data.decode("utf-8")))
