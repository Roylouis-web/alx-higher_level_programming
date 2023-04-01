#!/usr/bin/python3
"""
    a Python script that takes in a URL, sends a
    request to the URL and displays the body of
    the response (decoded in utf-8).
"""


import urllib.request
from urllib.error import HTTPError
import sys


try:
    with urllib.request.urlopen(sys.argv[1]) as f:
        print(f.read().decode())
except HTTPError as e:
    print('Error code: {}'.format(e.code))
