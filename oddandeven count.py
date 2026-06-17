n=int(input("enter n:"))
l=list(map(int,input(f"enter {n} elements\n").split()))
even=0;odd=0
for x in l:
    if x%2==0:
        even+=1
    else:
        odd+=1
print(l)
print("odd count:",odd)
print("even count:",even)
