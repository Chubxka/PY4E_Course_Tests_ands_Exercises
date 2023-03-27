import json
data= '''
[
    {"id" : "001",
    "x" : "2",
    "name" : "Quency"
    } ,
    {"id" : "009",
    "x" : "7",
    "name" : "Mrugesh"
    }
]
'''

info=json.loads(data)
for user in info:
    print('Name:',user['name'])
print('Name:', info[0]['x'])