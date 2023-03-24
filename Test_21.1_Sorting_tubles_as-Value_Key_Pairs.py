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
lst=list()
for k,v in count.items():#Creates a for loop for key,value pairs
    lst.append((v,k))#creates a list, where the values appended are added in the order value,key. Note that when adding multiple varieables as a tuple in a list, they must be contained within the tuple brackets.
lst=sorted(lst,reverse=True)#The list without the reverse true would sort in ascending order. With the reverse=True addition, the code sorts in decending order.
for v,k in lst[:100]:
    print(k,v)