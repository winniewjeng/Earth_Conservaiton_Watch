import re, sys, urllib, urllib.request, json, logging, os

# api_token = 'api_key=szvbj9zZLao7J4flDav0lgCJoQah0MUFCZEovD58'
url = 'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events'
#
# with urllib.request.urlopen('http://python.org/').open() as data:
# with urllib.request.urlopen("https://eonet.sci.gsfc.nasa.gov/api/v2.1/events") as url:
# http://maps.googleapis.com/maps/api/geocode/json?address=google

#     d = json.loads(data)
#     print(d)

import urllib.request, json
with urllib.request.urlopen("https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?api_key=szvbj9zZLao7J4flDav0lgCJoQah0MUFCZEovD58") as url:
    data = json.loads(url.read().decode())
    print(data)

# def response(url):
#     with urllib.request.urlopen(url) as response:
#         data = json.loads(url.read().decode())
#         print(data)
#         return data
#         # return response.read()
#
#
# if __name__ == "__main__":
#
#     url = 'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events'
#     response = json.loads(urllib.request.(url))
#     with urllib.request.urlopen(url) as response:
#         data = json.loads(api_url.read().decode())
#         print(data)

# response(api_url)
# response(api_url)

# with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
#     data = json.loads(url.read().decode())
#     print(data)
