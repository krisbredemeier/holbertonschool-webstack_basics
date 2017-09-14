#!/usr/bin/python3

'''
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the Github API,
here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
'''

import sys
import requests


def last_ten():
    '''
    Write a Python script that takes 2 arguments
    in order to solve this challenge.
    '''
    url = 'https://api.github.com/repos'
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url_repo = (url + owner_name + '/' + repo_name + '/' + 'commits')
    print(url_repo)
    urlr = requests.get(url_repo).json()
    top_ten = urlr[-10:]
    for commit in top_ten:
        print('{}: {}'.format(
            commit['sha'],
            commit['commit']['author']['name']
            ))

if __name__ == "__main__":
    last_ten()
