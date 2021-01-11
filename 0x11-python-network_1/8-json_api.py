#!/usr/bin/python3
""" Search API """
import requests
from sys import argv


if __name__ == "__main__":
    try:
        L = argv[1][0]
    except:
        L = ""
    info = {"q": L}
    r = requests.post("http://0.0.0.0:5000/search_user", data=info)
    try:
        data = r.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
