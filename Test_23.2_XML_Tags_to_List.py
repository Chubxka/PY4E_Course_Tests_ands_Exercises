import xml.etree.ElementTree as ET
#String contained within the code rather than input from a file. Note that usually this would come from a seperate file or server.
input='''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff=ET.fromstring(input)#Stuff becomes the input string we have created in the code.
lst=stuff.findall('users/user')#the list is formed of all tags within the parent tag users, and are of tag name user. In this case the list created has two users.
print('User Count:', len(lst))# Prints the length of the list. In this case there are two user tags, and therfore the list has a total length of 2.
for item in lst:
    print('Name:',item.find('name').text)#the .text addition at the end refines the code to only include the text contained within the opening and closing tag. If this was not included, both tags and the contained text would be included
    print('ID:',item.find('id').text)
    print('Attribute:', item.get("x"))