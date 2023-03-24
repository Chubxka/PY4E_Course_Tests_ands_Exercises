dd=dict()
names=['mike','john','sarah','becky','Mike','mike','sarah','glenn','jack']
for name in names: #for loop allows you to run through each element in the list with a variable name of 'name'
    dd[name]=dd.get(name,0)+1 #the get function will check if the name is within the dictionary. If it is, it will use its associatedd value; if not, it will use the default value of 0. In this case if a name isn't in the loop, it is added to the dictionary and givcen a value of 1.
print(dd)
