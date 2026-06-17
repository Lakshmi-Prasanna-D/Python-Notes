def automorphic(n):
    s=n**2
    v=str(s)
    t=n;
    c=0
    while(t!=0):
        c+=1;
        t/=10
    if(v.endswith(str(n))):
        return True
    return False
x=int(input("enter n:"))
if automorphic(x):
    print("automorphic")
else:
    print("not automorphic")

        
    
