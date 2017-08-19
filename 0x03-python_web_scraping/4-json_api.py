#!/usr/bin/python3

import requests
import sys

'''
Write a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON is the JSON is invalid
Display No result is the JSON is empty
You are not allowed to import packages other than requests and sys
'''

url = ('http://172.31.54.208:34955/search_user')
urlr = requests.get(url)

if (len(sys.argv) > 1):
    q = (sys.argv[1])
    # POST
    rp = requests.post(url, q)

    print(rp)
else:
    print('this')
