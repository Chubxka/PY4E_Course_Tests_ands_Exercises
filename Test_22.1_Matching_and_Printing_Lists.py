import re
z=0
x = 'My favourite 2 numbers are 26 and 22'
y=re.findall('[0-9]+',x)
print(y)
z=re.findall('[aeiou]+',x)
print(z)
a=re.findall('[AEIOU]+',x)
print(a)