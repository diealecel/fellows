# Diego Celis
# 28 October 2016
#
# This .py retrieves a dictionary and POST's the index of |needle| in |haystack|.

# API token: 72e05281a587a44918e768407d0f93d2
# Retrieve URL: http://challenge.code2040.org/api/haystack
# Post URL: http://challenge.code2040.org/api/haystack/validate

import requests # Needed for requests.

myToken = {'token':'72e05281a587a44918e768407d0f93d2'}
r = requests.post('http://challenge.code2040.org/api/haystack', json = myToken)

givenDict = eval(r.text) # Allows for a string to be implemented as code.
needle = givenDict['needle']
haystack = givenDict['haystack']

for bale in xrange(len(haystack)): # xrange used because index is needed.
    if haystack[bale] is needle:
        index = bale

result = {'token':myToken['token'], 'needle':index}
r = requests.post('http://challenge.code2040.org/api/haystack/validate', json = result)

print r.text # Ensure that test was passed.
