#!/usr/bin/python3

'''
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
'''

import requests
import sys

def post():
    '''
    intro to post
    '''
    # GET
    url = (sys.argv[1])
    urlr = requests.get(url)
    email = (sys.argv[2])

    # print(url)
    # print(email)

    # POST
    rp = requests.post(url, email)

    print('Your email is:', email)

if __name__ == "__main__":
    post()

# http://34.206.234.184:34955
