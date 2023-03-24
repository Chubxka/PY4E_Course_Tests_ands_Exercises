x=0
sum=0
for largest in [9,41,13,10,3,5,90,12,3,74,15]:
    sum = sum+largest
    x=x+1
    if largest>10:
        print('A Value above 10 was found =',largest)
print('The sum of the inputted values =',sum)
print('The loop executed',x,'times')
average=sum/x
print('The average of the values =',average)