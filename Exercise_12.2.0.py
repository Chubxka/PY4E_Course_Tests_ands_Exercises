# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
lst=list()


url = input('Enter URL- ')
count = input('Enter Count- ')
num=int(count)
position = input('Enter position- ')
pos=int(position)
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
print(tags)
while num > 0:
    wanted_url=tags[pos-1]
    url=wanted_url.get('href',2)
    print('Current URL:',url)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags=soup('a')
    num=num-1