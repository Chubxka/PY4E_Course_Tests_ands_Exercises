name=input('Enter file name: ')
if len(name) < 1:
    name = "mbox-short.txt"
try:
    fh=open(name)
except:
    print('the file name entered could not be found. Please restart the program and enter a valid file name.')
    quit()
counts=dict()
lst=list()
for line in fh:
    if line.startswith('From '):
        words=line.split()
        for word in words:
            if ':' in word:
                times=word.split(':')
                hours=times[0]
                counts[hours]=counts.get(hours,0)+1
for k,v in counts.items():
    lst.append((k,v))
    sort=lst.sort()
for v,k in lst:
    print(v,k)