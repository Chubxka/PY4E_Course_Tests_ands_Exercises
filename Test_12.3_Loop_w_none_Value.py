x=None
for smallest in [9,41,12,3,74,15,104,345,2,3,4,1,2]:
    if x is None:
        x=smallest
    elif smallest<x:
        x=smallest
print(x)