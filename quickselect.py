def quickselect(a,l,h):
    pi=a[h]
    pl=l
    for i in range(l,h):
        if a[i]<pi:            
            a[i],a[pl]=a[pl],a[i]
            pl+=1           
    a[pl],a[h]=a[h],a[pl]
    return pl
    

def kthsmallest(a,l,h,k):
    pi=quickselect(a,l,h)
    if pi==k-1:
        return a[pi]
    elif pi>k-1:
        return  kthsmallest(a,l,pi-1,k)
    else:
        return kthsmallest(a,pi+1,h,k)


n=int(input("enter n value:"))
l=[]
print(f"enter {n} elements")
l=list(map(int,input().split()))
print(l)
    
k=int(input("enter k value"))
if(k>n or k<=0):
    print('invalid')
else:
    x=kthsmallest(l,0,n-1,k)
    print(f"{k}th value is:{x}")
    
