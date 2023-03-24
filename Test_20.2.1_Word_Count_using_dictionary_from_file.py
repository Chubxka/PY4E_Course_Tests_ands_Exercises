file=input('What is the file name:  ')
try:
    fh=open(file)
except:
    print('File could not be found, please restart the program and input a valid file name.')
    quit()
count=dict()
for line in fh:
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1
bigcount=None
bigword=None
for key,cnt in count.items():
    if bigcount is None or cnt > bigcount:
        bigword=key
        bigcount=cnt
print(bigword,bigcount)