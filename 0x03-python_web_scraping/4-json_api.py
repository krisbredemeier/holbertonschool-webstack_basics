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


def search():
    '''
    searches through json for id and name
    '''
    url = ('http://0.0.0.0:5000/search_user/search_user')
    if (len(sys.argv) > 1):
        q = (sys.argv[1])
    else:
        q = ("")
        print('No result')
    urlr = requests.post(url, data={'q': q}).json()
        # try:
        #     url = ('http://0.0.0.0:5000/search_user/search_user')
        #     urlr = requests.post(url, data={'q': q}).json()
        # except:
        #     print('Not a valid JSON')

    if ('id' and 'name' not in urlr):
        print('No result')
    else:
        try:
            print('[{}] {}'.format(urlr['id'], urlr['name']))
        except:
            print('Not a valid JSON')

if __name__ == "__main__":
    search()
