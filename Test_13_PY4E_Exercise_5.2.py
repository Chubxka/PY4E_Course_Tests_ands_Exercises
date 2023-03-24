largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            value = float(num)
            if largest is None:
                largest=value
                smallest=value
            elif value<smallest:
                smallest=value
            elif value>largest:
                largest=value
        except:
            print('invalid input')
largest=int(largest)
smallest=int(smallest)
print("Maximum is", largest)
print('Minimum is', smallest)