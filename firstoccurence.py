#index of first occurence
print("enter elements:")
l=list(map(int,input().split()))
print("enter x value:")
x=int(input())
n=len(l)
res=-1
for i in range(n):
    if l[i]==x:
        res=i
        break
print("index is:",res)
