#!/usr/bin/python3

'''
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
'''

import requests
import sys


def post(peram):
    '''
    intro to post
    '''
    # GET
    url = peram[1]
    email = {'email': peram[2]}

    # POST
    rp = requests.post(url, email)

    # print('Your email is:', email)
    print(response.text)

if __name__ == "__main__":
    perams = sys.argv
    post(perams)
