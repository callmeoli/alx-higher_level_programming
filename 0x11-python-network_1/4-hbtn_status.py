#!/usr/bin/python3
""" py script that fetch ALX-intranet"""

import requests

if __name__ == "__main__":
    """ the funciton is here below """
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url).text
    print('Body response:')
    print('\t- type: {}'.format(type(r)))
    print('\t- content: {}'.format(r))
