fname=input('What is the file name:  ')
count=0
try:
    fh=open(fname)
except:
    print('The file could not be found, please input a valid file name')
    quit()
for line in fh:
    if line.startswith('From '):
        count=count+1
        sline=line.split()
        print(sline[1])
print(count)