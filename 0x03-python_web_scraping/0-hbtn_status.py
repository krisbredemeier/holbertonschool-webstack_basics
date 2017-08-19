#!/usr/bin/python3

'''
Write a Python script that fetches https://intranet.hbtn.io/status
'''

import requests

def status():
    '''
    beginning with get response
    '''
    r = requests.get("https://intranet.hbtn.io/status")
    t = (type(r.text))
    c = r.text
    print('Body response:')
    print('    - type:', t)
    print('    - content:', c)

if __name__ == "__main__":
    status()
