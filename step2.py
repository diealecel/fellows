# Diego Celis
# 28 October 2016
# 
# This .py retrieves a string and POST's its reverse.

# API token: 72e05281a587a44918e768407d0f93d2
# Retrieve URL: http://challenge.code2040.org/api/reverse
# Post URL: http://challenge.code2040.org/api/reverse/validate

import requests # Needed for requests.

myToken = {'token':'72e05281a587a44918e768407d0f93d2'}
r = requests.post('http://challenge.code2040.org/api/reverse', json = myToken)
product = r.text[::-1] # Takes advantage of the interval notation in Python, [start:end:interval].
r = requests.post('http://challenge.code2040.org/api/reverse/validate', json = {'token':myToken['token'], 'string':product})

print r.text # Ensure that test was passed.
