fname = input('What is the file name:   ')
try:
    file=open(fname)
except:
    print('File',"'",fname,"'", 'cannot be found')
    #Without this quit, the file would continue and cause a traceback at line 9 as the variable file is not properly defined.
    #Note that the quit option will end the whole python code.
    quit()
count=0
for line in file:
    count=count+1
    line=line.rstrip()
    if line.startswith('From'):
        print(line[0:4])
        x=line.count('From')
        print(x)
    if not 'python' in line:
        continue
    print(line)
print(count)