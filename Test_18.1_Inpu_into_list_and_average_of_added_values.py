numblist=list()
while True:
    inp=input('What is the number: ')
    if inp == 'done':
        break
    else:
        try:
            value=float(inp)
            numblist.append(value)
        except:
            print('This is not a number, please enter a valid number')
            continue
average = sum(numblist)/len(numblist)
print(average)