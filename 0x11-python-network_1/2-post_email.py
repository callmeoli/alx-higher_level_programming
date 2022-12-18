#!/usr/bin/python3
""" take url and display  of X-Reques-Id """
import sys
import urllib

url = sys.argv[1]
values = {'email': sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
req = urllib.request.Request(url, data)
if __name__ == "__main__":
    """ take url and display X-Reques-Id """
    with urllib.request.urlopen(req) \
            as response:
        page = response.read()
    print(page)
