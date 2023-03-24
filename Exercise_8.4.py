fname=input('What is the file name:  ')
fh=open(fname)
lst=list()
for line in fh:
    wlist=line.split()
    for word in wlist:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)