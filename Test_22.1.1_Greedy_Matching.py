import re
x= 'From: james.clear@uct.ac.za : Using the: character '
y=re.findall('^F.+:',x)#Greedy variant of the matching
z=re.findall('^F.+?:',x)#Non-Greedy Variant of the matching
a=re.findall('\S*@\S*',x)#A number of non-whitespace characters before and after the '@'
b=re.findall('^From: (\S*@\S*)',x)#The extraction of the string only occurs for what is contained within the parenthesis.
print(y)
print(z)
print(a)
print(b)