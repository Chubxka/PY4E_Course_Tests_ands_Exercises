temp = input('What is the temperature in farenheit?')
cel = 0
try:
    fahr = float(temp)
    if fahr>=10:
        print('temp is 10 or more')
    else:
        print('temp is less than 10')
except:
    fahr=0
    print('Why is it',temp,'?')
cel = (fahr-32.0)*5.0/9.0
print(cel)
