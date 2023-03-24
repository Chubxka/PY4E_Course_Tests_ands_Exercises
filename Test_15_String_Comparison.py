fruit='banana'
while True:
    word=input('What is a fruit you ate today?')
    if word == 'done':
        break
    elif word < fruit:
        print('Your fruit is before banana when arranged in alphabetical order.')
    elif word > fruit:
        print('Your fruit comes after banana when arranged in alphabetical order.')
print('Thank you, Goodbye')