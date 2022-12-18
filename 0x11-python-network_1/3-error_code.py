#!/usr/bin/python3
""" script that take url and send request and display"""

import sys
from urllib import request, parse, error

if __name__ == "__main__":
    """ the function """
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            page = response.read().decode('utf-8')
            print(page)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
