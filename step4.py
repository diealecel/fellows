# Diego Celis
# 28 October 2016
#
# This .py retrieves a dictionary and POST's an array with all words in |array| without the prefix |prefix|.

# API token: 72e05281a587a44918e768407d0f93d2
# Retrieve URL: http://challenge.code2040.org/api/prefix
# Post URL: http://challenge.code2040.org/api/prefix/validate

import requests # Needed for requests.

myToken = {'token':'72e05281a587a44918e768407d0f93d2'}
r = requests.post('http://challenge.code2040.org/api/prefix', json = myToken)

givenDict = eval(r.text) # Allows for a string to be implemented as code.
prefix = givenDict['prefix']
array = givenDict['array']

result = []

for word in array:
    if word.find(prefix) != 0: # If |prefix| is not found exactly as the prefix, then...
        result.append(word)

final = {'token':myToken['token'], 'array':result}
r = requests.post('http://challenge.code2040.org/api/prefix/validate', json = final)

print r.text # Ensure that test was passed.
