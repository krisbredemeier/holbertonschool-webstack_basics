#!/usr/bin/python3

'''
Write a Python script that takes in a string
and sends a search request to the Star Wars API
'''


def starwars():
    '''
    all of the planets
    '''
    import requests
    import sys

    person = sys.argv[1]
    url = ('https://swapi.co/api/people/')
    urlr = requests.get(url, params={'search': person}).json()

    print('Number of result: {}'.format(urlr['count']))
    # count the number of resturns
    for name in urlr['results']:
        print(name['name'])

if __name__ == "__main__":
    starwars()
