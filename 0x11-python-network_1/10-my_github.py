#!/usr/bin/python3
"""
    a Python script that takes your GitHub
    credentials (username and password)
    and uses the GitHub API to display your id
"""


from requests.auth import HTTPBasicAuth
import requests
import sys


response = requests.get('https://api.github.com/user',
                        auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
print(response.json()['id'])
