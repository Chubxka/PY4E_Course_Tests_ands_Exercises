import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count=0
total=0

while True:
    url = input('Enter XML File: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')#This prints out the number of characters that are present within the XML file. Note this is prior to decoding
    print(data.decode())#This prints the decoded data that has been collected from the inputed url
    tree = ET.fromstring(data)#this section parses through all the data extracted from the xml file

    results = tree.findall('.//comment')#This finds all the 
    for i in results:
        num=i.find('count').text
        count=count+1
        total=total+int(num)
print('Count:',count)
print('Sum:',total)