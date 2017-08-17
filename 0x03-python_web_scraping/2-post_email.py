#!/usr/bin/python3

import requests
import sys

'''
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
'''

url = (sys.argv[1])
email = (sys.argv[2])
# h = requests.get(sys.argv[1])

# url.requests("POST", email)
h = requests.post(email)
print('Your email is:', email)
# print(url)
# print(email)
