#!/usr/bin/python3
"""post email to url provided"""

from sys import argv
import requests

if __name__ == "__main__":
    """ fuction for module """
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
