l=list(map(int,input("enter elements:\n").split()))
print(l)
n=len(l)
res=[]
for i in range(1,n):
    if l[i]!=l[i-1]:
        res.append(l[i-1])
if l[-1] not in res:
    res.append(l[-1])
print("removed duplicates:\n")
print(res)
