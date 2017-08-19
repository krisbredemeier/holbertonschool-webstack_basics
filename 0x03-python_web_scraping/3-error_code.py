#!/usr/bin/python3

import requests
import sys

'''
Write a Python script that takes in a URL,
sends a request to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
'''
url = (sys.argv[1])
urlr = requests.get(url)

if (urlr.status_code >= 400):
    print('Error code: ', urlr.status_code)
else:
    print(urlr.text)
