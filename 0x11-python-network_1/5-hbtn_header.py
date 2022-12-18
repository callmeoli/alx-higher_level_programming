#!/usr/bin/python3
""" This module take script and display variable X-Request-Id"""

from sys import argv
import requests

if __name__ == "__main__":
    """ the function below """
    head = requests.get(argv[1]).headers
    print(head["X-Request-Id"])
