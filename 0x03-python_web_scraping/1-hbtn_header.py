#!/usr/bin/python3

import requests
import sys

'''
Write a Python script that takes in a URL, sends a request
to the URL and displays the value of the variable X-Request-Id
in the response header
'''

h = requests.get(sys.argv[1])
print(h.headers['x-request-id'])
