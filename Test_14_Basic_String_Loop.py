fruit='banana'
num=0
while num<len(fruit):
    print(num,fruit[num])
    num=num+1
print('The while loop has been processed')
#The 'for' loop is a more efficient version of the while loop as it contains less lines of codes to complete the same task as that of the while loop.
for letter in fruit:
    print(letter)
print('The for loop has been processed')
