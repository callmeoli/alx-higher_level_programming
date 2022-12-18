#!/usr/bin/python3
""" this module take URL and send request URL"""
from sys import argv
import requests

if __name__ == "__main__":
    """the function here below"""
    url = argv[1]
    try:
        res = requests.get(url)
        code = res.status_code
        print(res.text)
    except requests.HTTPError as err:
        print("Error code: {}".format(code))
