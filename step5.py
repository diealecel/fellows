# Diego Celis
# 28 October 2016
#
# This .py retrieves a date in ISO 8601 format and POST's a string in the same format, but changed by adding |interval|.

# API token: 72e05281a587a44918e768407d0f93d2
# Retrieve information: http://challenge.code2040.org/api/dating
# Post information: http://challenge.code2040.org/api/dating/validate

import requests                # Needed for requests.
from datetime import datetime  # Needed for creating datetime object.
from datetime import timedelta # Needed for adding |interval|.

myToken = {'token':'72e05281a587a44918e768407d0f93d2'}
r = requests.post('http://challenge.code2040.org/api/dating', data = myToken)

givenDict = eval(r.text) # Allows for a string to be implemented as code.
datestamp = givenDict['datestamp']
interval = givenDict['interval']

# Break up |datestamp| into components.
date = datestamp[0:datestamp.find('T')]
time = datestamp[datestamp.find('T') + 1:len(datestamp) - 1]

# |date| = 2016-11-28
# |time| = 06:08:57

# Retrieve individual numbers as strings.
year = date[:date.find('-')]
month = date[date.find('-') + 1:date.rfind('-')]
day = date[date.rfind('-') + 1:]
hour = time[:time.find(':')]
minute = time[time.find(':') + 1:time.rfind(':')]
second = time[time.rfind(':') + 1:]

# Convert all strings into int's.
year = int(year)
month = int(month)
day = int(day)
hour = int(hour)
minute = int(minute)
second = int(second)

# Create datetime object, add |interval|, and then turn into a string.
result = str(datetime(year, month, day, hour, minute, second) + timedelta(seconds = int(interval)))

# Change |result| into ISO 8601 format.
result = result[:result.find(' ')] + 'T' + result[result.find(' ') + 1:] + 'Z'

final = {'token':myToken['token'], 'datestamp':result}
r = requests.post('http://challenge.code2040.org/api/dating/validate', data = final)

print r.text # Ensure that test was passed.
