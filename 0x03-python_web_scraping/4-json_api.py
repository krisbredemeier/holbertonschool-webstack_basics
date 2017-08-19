#!/usr/bin/python3

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

import requests
import sys


if (len(sys.argv) > 1):
    q = (sys.argv[1])
    url = ('http://34.206.234.184:34955/search_user')
    # POST
    urlr = requests.post(url, data={ 'q': q }).json()
    # print(url)
    # print(urlr)
    print(urlr['id'], urlr['name'])

    # if (j):
    #     print('[{}]', id, name)
else:
    q = ("")
    print('No result')
