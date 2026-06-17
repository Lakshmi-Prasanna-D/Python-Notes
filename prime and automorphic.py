def isprime(n):
    if n<2:
        return false
    for i in range (2,n//2 +1):
        if n%i==0:
            return False;
    return True
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
print("select your choice:")
print("1:Automorphic")
print("2. Check Prime")

ch=int(input())
match(ch):
    case 1:        
        if automorphic(x):
            print("automorphic")  
        else:
            print("not automorphic")
    case 2:
        if isprime(x):
            print("prime")
        else:
            print("not prime")
    case _:
        print("invalid choice")

        
    
