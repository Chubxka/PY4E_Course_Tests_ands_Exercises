def computepay():
    h=input("How many hours did you work?")
    r=input('What is the rate for these hours?')
    hrs=float(h)
    rt=float(r)
    if hrs>40:
        pay=(40*rt)+((hrs-40)*(rt*1.5))
    else:
        pay=(hrs*rt)
    return(pay)
p=computepay()
print('Your pay is',p)