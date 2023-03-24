fname = input('What is the file name:   ')
count=0
tot=0
try:
    file=open(fname)
except:
    print('File',"'",fname,"'", 'cannot be found')
    #Without this quit, the file would continue and cause a traceback at line 9 as the variable file is not properly defined.
    #Note that the quit option will end the whole python code.
    quit()
for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        count=count+1
        numstart=line.find('0')
        num=line[numstart:]
        numb=float(num)
        tot=tot+numb
    else:
        continue
average=tot/count
print(count)
print(average)