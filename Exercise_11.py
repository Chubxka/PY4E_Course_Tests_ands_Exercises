import re
sum=0
count=0
fh=open('Exercise_11_Text_2.txt')
for lines in fh:
    x=re.findall('[0-9]+',lines)
    for num in x:
        z=int(num)
        count=count+1
        sum=sum+z
print(sum)
print(count)