#!/usr/bin/python3

import sys
import requests

def last_ten():
    url = 'https://api.github.com/repos'
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url_repo = (url + owner_name + '/' + repo_name + '/' + 'commits')
    print(url_repo)
    urlr = requests.get(url_repo).json()
    # top = urlr[10]
    for commit in range(10):
        print('{}: {}'.format(commit['sha'], commit['commit']['author']['name']))

if __name__ == "__main__":
    last_ten()
