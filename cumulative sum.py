#cumulative sum
l=list(map(int,input(f"enter elements\n").split()))
csum=[]
v=0
for x in l:
    v+=x
    csum.append(v)
print("the cumulative sum is",csum)
#cumulative product
cprod=[]
v=1;
for x in l:
    v*=x;
    cprod.append(v)
print("cumulative product is",cprod)
    
