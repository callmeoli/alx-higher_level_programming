#!/usr/bin/python3
""" Py script that take letter as param and sent it to web
    http://0.0.0.0:5000/search_user
"""
from sys import argv
import requests

if __name__ == "__main__":
    """ the function here bellow"""
    if len(argv) == 1:
        req = requests.post('http://0.0.0.0:5000/search_user', data={q=""})
        if (type(req) == 'json' and req is not None):
            for k, v in req:
                print('[{}] {}'.format(k, v))
        else:
            print("No result")
    else:
        req = requests.post('http://0.0.0.0:5000/search_user',
                            data={q=argv[1]})
        if (type(req) == 'json' and req is not None):
            for k, v in req:
                print('[{}] {}'.format(k, v))
        else:
            print("No result")
