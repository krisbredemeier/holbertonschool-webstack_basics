#!/usr/bin/python3

import requests
import sys

'''

'''
url = (sys.argv[1])
urlr = requests.get(url)

print(urlr.text)
