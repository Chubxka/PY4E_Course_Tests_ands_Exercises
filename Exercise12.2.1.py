# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
sum=0
lst=list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
lst=0
url = input('Enter - ')
iter=input('Enter number of iterations: ')
count=int(iter)
count=count-1
num=count
position=input('Enter the position of the URL: ')
pos=int(position)-1
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
while True:
    tags=soup('a')
    if (num+1) == 0:
        break
    elif lst>pos:
        url=current_url
        html = urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        tags=soup('a')
        num=num-1
        lst=0
    else:
        for tag in tags:
            if (pos+1)>lst:
                url=tag.get('href',None)
                current_url=url
                lst=lst+1
        print(url)