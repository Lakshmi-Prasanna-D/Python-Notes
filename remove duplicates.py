l=list(map(int,input("enter elements:\n").split()))
print(l)
n=len(l)
res=[]
for x in l:
    if x not in res:
        res.append(x)
print("removed duplicates:\n")
print(res)
