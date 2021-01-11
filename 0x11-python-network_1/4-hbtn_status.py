#!/usr/bin/python3
""" What's my status? #1 """
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    data = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(data.text)))
    print("\t- content: {}".format(data.text))
