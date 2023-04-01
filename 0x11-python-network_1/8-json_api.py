#!/usr/bin/python3
"""
   a Python script that takes in
   a letter and sends a POST request
   to http://0.0.0.0:5000/search_user
   with the letter as a parameter.
"""


import requests
import sys


if len(sys.argv) == 2:
    dic = {"q": sys.argv[1]}
else:
    dic = {"q": ''}

response = requests.post('http://0.0.0.0:5000/search_user', dic)
if response.json():
    _id = response.json()['id']
    name = response.json()['name']
    print('[{}] {}'.format(_id, name))
else:
    print('No record')
