import re
file=open('mbox-short.txt')
count=0
for line in file:
    line = line.rstrip()
    if re.search('From',line):#This regular expression matches the string in line and prints the found line.
        count=count+1
        print(line)
    if re.search('^X.*:',line):#This will match the X at the beginning of a line, followed by 0 or more characters, with the end being a colon.
        print(line)
print(count)