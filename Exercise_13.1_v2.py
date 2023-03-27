import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

count=0
total=0

while True:
    url = input('Enter XML File: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    data = uh.read()
    print('Retrieved', len(data), 'characters')#This prints out the number of characters that are present within the XML file. Note this is prior to decoding
    print(data.decode())#This prints the decoded data that has been collected from the inputed url
    tree = ET.fromstring(data)#this section parses through all the data extracted from the xml file

    results = tree.findall('.//count')#This section goes through the tree and finds all the tags that are named 'count'. Note that results becomes a list of all the tags found in order.
    for i in results:
        count=count+1
        total=total+int(i.text)#This part of the code takes the individual found tag from the list produced (results), and transforms the string contained within the tags into an integer, which provides the sum of all the numbers.
    print(count)
    print(total)