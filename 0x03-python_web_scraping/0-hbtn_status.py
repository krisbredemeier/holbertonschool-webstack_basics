#!/usr/bin/python3
'''
Write a Python script that fetches https://intranet.hbtn.io/status
'''

import requests
r = requests.get("https://intranet.hbtn.io/status")
t = (type(r.text))
c = r.text
print('    - type: {}', t)
print('    - content: {}', c)
