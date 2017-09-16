#!/usr/bin/python3

'''
Write a Python script that takes in a string
and sends a search request to the Star Wars API
'''

import sys
import requests


def sw_api():
    '''
    Write a Python script that takes in a string
    and sends a search request to the Star Wars API
    '''

    person = sys.argv[1]
    url = ('https://swapi.co/api/people/')
    urlr = requests.get(url, params={'search': person}).json()
    # peram = urlr['results']
    print('Number of results: {}'.format(urlr['count']))

    for name in urlr['results']:
        print(name['name'])

    if (urlr['next'] is not None):
        urlr = requests.get(urlr['next']).json()
        while urlr['next'] is not None:
            for name in urlr['results']:
                print(name['name'])
                urlr = requests.get(urlr['next']).json()
        for name in urlr['results']:
            print(name['name'])


if __name__ == "__main__":
    sw_api()
