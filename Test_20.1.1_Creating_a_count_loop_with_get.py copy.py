dd=dict()
names=['mike','john','sarah','becky','Mike','mike','sarah','glenn','jack']
for name in names:
    dd[name]=dd.get(name,0)+1
print(dd)
