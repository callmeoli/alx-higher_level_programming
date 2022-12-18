#!/usr/bin/python3
""" Py script that take letter as param and sent it to web
    http://0.0.0.0:5000/search_user
"""
from sys import argv
import requests

if __name__ == "__main__":
    """ the function here bellow"""
    q_value = "" if len(argv) == 1 else argv[1]
    values = {'q'=q_value }
    url = http://0.0.0.0:5000/search_user
    response = requests.post(url, values)
    try:
        json = resp.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
