file=input('What is the file name:  ')
if len(file) < 1:
    file='romeo.txt'
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
print(sorted([(v,k) for k,v in count.items()],reverse=True))