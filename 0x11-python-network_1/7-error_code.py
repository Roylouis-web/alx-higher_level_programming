#!/usr/bin/python3
"""
    a Python script that takes in a URL,
    sends a request to the URL
    and displays the body of the response.
"""


import requests
import sys


response = requests.get(sys.argv[1])
print('Error code: {}'.format(response.status_code))
