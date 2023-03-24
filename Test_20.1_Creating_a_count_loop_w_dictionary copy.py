dd=dict()
names=['mike','john','sarah','becky','Mike','mike','sarah','glenn','jack']
for name in names:
    if name not in dd:
        dd[name]=1
    else:
        dd[name]=dd[name]+1
print(dd)
dd['luca']=dd.get('luca',0)+1
print(dd)
