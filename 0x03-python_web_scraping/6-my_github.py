#!/usr/bin/python3

'''
Write a Python script
that takes your Github credentials (username and password)
and uses the Github API to display your id
'''


def github():
    '''
    Github
    '''

    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    user = sys.argv[1]
    password = sys.argv[2]
    url = ('https://api.github.com/user')
    urlr = requests.get(url, auth=(user, password)).json()
    print(urlr.get('id'))

if __name__ == "__main__":
    github()
