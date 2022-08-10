# Import the requests library so that we can use the get method
# Import the json library
import requests
import json

# Make a call to Sunrise Sunset API
# Attribution/credit here: https://sunrise-sunset.org/api

# eventually do something with these
time_zone = 'west'
lat = '37.133955'
lng = '-119.48963'
# Print out the results returned in JSON

result = requests.get('http://api.sunrise-sunset.org/json?lat=37.133955&lng=-119.48963&date=today&formatted=1')

mystring = json.dumps(result.text)
# mydict = json.loads(result.text)
#for key, value in mydict.items():
#    print(key, ' : ', value)
#    print("\n")
# print(mystring)

# The below code won't work correctly whenever a UTC time has a double digit
# for the hour... this is super lazy. Consider using a dictionary, and also
# ability to convert time zone to appropriate. 
sunrise = mystring[29:39]
sunset = mystring[55:65]
print('\n')
print(f"Sunrise occurs at {sunrise}, UTC")
print(f"Sunset occurs at {sunset}, UTC")
print('\n')
