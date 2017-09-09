#!/usr/bin/python3

'''
Write a Python script that takes in a string
and sends a search request to the Star Wars API
'''

import sys
import requests


def sw_api(perams):
    '''
    Write a Python script that takes in a string
    and sends a search request to the Star Wars API
    '''

    peram = perams['results']

    for name in peram:
        print(name['name'])

    if (perams['next'] is not None):
        urlr = requests.get(perams['next']).json()
        sw_api(perams)
    # person = sys.argv[1]



    # count the number of resturns
    # for name in urlr['results']:
    #     print(name['name'])

if __name__ == "__main__":
    person = sys.argv[1]
    url = ('https://swapi.co/api/people')
    urlr = requests.get(url, params={ 'search': person }).json()
    print('Number of results: {}'.format(urlr['count']))
    sw_api(person)
