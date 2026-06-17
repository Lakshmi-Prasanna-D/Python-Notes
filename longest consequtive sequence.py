l=list(map(int,input("enter the elemens:\n").split()))
l=sorted(l)
#l=set(l)
n=len(l)
c=1
m=0
for i in range(1,n):
    if l[i]-l[i-1]==1:
        c+=1
    elif l[i]==l[i-1]:
        continue
    else:
        m=max([m,c])
        c=1
m=max([m,c])
print("max count is",m)
