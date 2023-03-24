hrs = input("Enter Hours:")
h = float(hrs)
r = 10.50
if h<40:
    pay=h*r
    print('your rate is',pay)
else:
    pay=h*(10.50*1.5)
    print('Your pay is',pay)
print(pay)