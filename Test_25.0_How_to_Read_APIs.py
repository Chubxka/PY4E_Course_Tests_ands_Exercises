import urllib.request, urllib.parse, urllib.error
import json

serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address=input('Enter loaction: ')
    if len(address)<1: break
    url=serviceurl+urllib.parse.urlencode({'address':address})
    print('Retrieving',url)
    uh=urllib.request.urlopen(url)
    data= uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js=json.loads(data)
    except:
        js=None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure to Retrieve ====')
        print(data)
        continue

    lat=js["results"][0]["geometry"]["location"]["lat"]
    lng=js["results"][0]["geometry"]["location"]["lng"]
    print('lat',lat,'lng',lng)
    location=js['results'][0]['formatted_address']
    print(location)

#This following code is the returned value from JSON if the loaction inputted is Ann Arbour, MI

'''
"status": "OK",
"results": [
    {
        "geometry": {
            "location_type":"APPROXIMATE",
            "location":{
                "lat":42.2808256,
                "lng":-83.7430378
            }
        },
        "address_components":[
            {
                "long_name": "Ann Arbor",
                "types":[
                    "locality"
                    "political"
            ],
            "short_name": "Ann Arbor"
        }
       ],
       "formatted_address": "Ann Arbor, MI, USA",
       "types":[
        "locality",
        "political"
       ]
    }
]
'''