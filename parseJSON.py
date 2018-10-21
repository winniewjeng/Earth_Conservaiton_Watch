import urllib.request, json


# if __name__ == "__main__":
# api_token = 'api_key=szvbj9zZLao7J4flDav0lgCJoQah0MUFCZEovD58'
url = 'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events'
#
# with urllib.request.urlopen('http://python.org/').open() as data:
# with urllib.request.urlopen("https://eonet.sci.gsfc.nasa.gov/api/v2.1/events") as url:
#     d = json.loads(data)
#     print(d)

event_dict = {}

with urllib.request.urlopen(
        "https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?api_key=szvbj9zZLao7J4flDav0lgCJoQah0MUFCZEovD58") as url:
    data = json.loads(url.read().decode())
    # print(data)
    count = 0
    for i in data['events']:

        # print(data['events'][count]['title'])
        # print(data['events'][count]['geometries'][0]['coordinates'][0])  # long
        # try:
        #     print(data['events'][count]['geometries'][0]['coordinates'][1])  # lat
        # except IndexError:
        #     print('No second coordinate')
        try:
            # create a tuple as event_dict key that contains my logitude and latitude
            coord = (data['events'][count]['geometries'][0]['coordinates'][0],
                     data['events'][count]['geometries'][0]['coordinates'][1])
            event = data['events'][count]['title']
            coord = str(coord)
            event_dict.update({coord: event})
        except IndexError:
            pass
        # print(event_dict)
        count = count + 1

    for i in event_dict:
        item = event_dict[i]
        print(item, i)


    with open('result.json', 'w') as fp:
        json.dump(event_dict, fp)

    fp.close()

    # test if point is inside a polygon
    # convert a dictionary to cvs file


    # print(len(event_dict))

        # print(event_dict[i])


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
