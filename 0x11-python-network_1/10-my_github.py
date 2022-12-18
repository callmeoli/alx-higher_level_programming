#!/usr/bin/python3
""" Py script that connect to github suing autentiction"""
import sys
import requests

if __name__ == "__main__":
    """ this is the  """
    url = 'https://api.github.com/user'
    resp = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    try:
        json = resp.json()
        if json:
            print("{}".format(json.get('id')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
