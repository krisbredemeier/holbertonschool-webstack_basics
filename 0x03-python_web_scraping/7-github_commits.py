#!/usr/bin/python3

import sys
import requests

def last_ten():
    url = 'https://api.github.com/repos/rails/rails/commits'
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    urlr = requests.get(url, auth=(repo_name, owner_name)).json()
    top = urlr[:10]
    for commit in top:
        print('{}:{}'.format(commit['sha'], commit['commit']['author']['name']))

if __name__ == "__main__":
    last_ten()
