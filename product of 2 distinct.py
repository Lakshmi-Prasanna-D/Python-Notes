l=list(map(int,input().split()))
prod=1;
maxprod=1;
l.sort()
n=len(l)
prod*=l[-1]
i=n-1
while(
