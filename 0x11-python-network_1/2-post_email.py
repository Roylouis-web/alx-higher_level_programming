#!/usr/bin/python3
"""
    a Python script that takes in a URL and an email,
    sends a POST request to the passed URL with the email
    as a parameter, and displays the body of the
    response (decoded in utf-8)
"""


import urllib.request
import urllib.parse
import sys

data = urllib.parse.urlencode({'email': sys.argv[2]})
data = data.encode('ascii')
with urllib.request.urlopen(sys.argv[1], data) as f:
    print(f.read().decode())
