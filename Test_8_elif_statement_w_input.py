#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade
score = input("Enter Score: ")
scr = float (score)
if scr <= 1.0:
    if scr >= 0.9:
        print('A')
    elif scr >= 0.8:
        print('B')
    elif scr >= 0.7:
        print('C')
    elif scr >= 0.6:
        print('D')
    elif scr < 0.6:
        print('F')
else:
    print('Score not valid')
print('All Done')