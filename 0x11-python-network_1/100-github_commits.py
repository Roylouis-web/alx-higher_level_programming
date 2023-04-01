#!/usr/bin/python3
"""
    a Python script that takes 2 arguments
    in order to solve this challenge.
"""
# /repos/{owner}/{repo}/commits

import requests
import sys


response = requests.get('https://api.github.com/repos/{}/{}/commits'
                        .format(sys.argv[1], sys.argv[2]))
i = 1
for dic in response.json():
    print('{}: {}'.format(dic['sha'], dic['commit']['author']['name']))
    if i == 10:
        exit()
    i += 1
