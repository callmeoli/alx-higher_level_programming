#!/usr/bin/python3
""" take url and display X-Reques-Id """
from sys import argv
import urllib

url = argv[1]
values = {'email': argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
if __name__ == "__main__":
    """ take url and display X-Reques-Id """
    with urllib.request.urlopen(req) \
            as response:
        page = response.read()
    print(page)
