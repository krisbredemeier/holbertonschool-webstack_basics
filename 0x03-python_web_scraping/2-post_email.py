#!/usr/bin/python3

import requests
import sys

'''
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
'''


# GET
url = requests.get(sys.argv[1])
email = requests.get(sys.argv[2])
# url = (sys.argv[1])
# email = (sys.argv[2])

print(url)
print(email)

# POST
# rp = requests.post(url, email)

# response, status
# print(url.text)
# print(email.text)
# print(rp.text)
# print(url.status_code)
# print(rp.status_code)




# url.requests("POST", email)
# h = requests.post(email)
# print('Your email is:', email)
# print(url)
# print(email)
