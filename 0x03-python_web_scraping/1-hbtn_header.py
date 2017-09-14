#!/usr/bin/python3

'''
Write a Python script that takes in a URL, sends a request
to the URL and displays the value of the variable X-Request-Id
in the response header
'''

import requests
import sys


def response():
    '''
    prints header response
    '''
    h = requests.get(sys.argv[1])
    print(h.headers.get('X-Request-Id'))

if __name__ == "__main__":
    response()
