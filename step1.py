# Diego Celis
# 28 October 2016
# 
# This .py registers me into the API.

# API token: 72e05281a587a44918e768407d0f93d2
# Post URL: http://challenge.code2040.org/api/register

import requests # Needed for requests.

requestedDict = {'token':'72e05281a587a44918e768407d0f93d2', 'github':'https://github.com/diealecel/fellows'}
r = requests.post('http://challenge.code2040.org/api/register', json = requestedDict)

print r.text # Ensure that test was passed.
