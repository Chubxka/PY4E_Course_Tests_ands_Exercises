name=input('Enter file name: ')
if len(name) < 1:
    name = "mbox-short.txt"
try:
    fh=open(name)
except:
    print('the file name entered could not be found. Please restart the program and enter a valid file name.')
    quit()
counts=dict()
for line in fh:
    if line.startswith('From '):
        words=line.split()
        for word in words:
            if '@' in word:
                counts[word]=counts.get(word,0)+1
print(counts)
bigsender=None
bigcount=None
for key,val in counts.items():
    if bigsender==None or val>bigcount:
        bigsender=key
        bigcount=val
print(bigsender,bigcount)