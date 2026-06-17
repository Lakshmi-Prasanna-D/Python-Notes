def isprime(n):
    if n<2:
        return false
    for i in range (2,n//2 +1):
        if n%i==0:
            return False;
    return True
def displayprimes(n):
    for i in range (2,n+1):
        if isprime(i):
            print(i,end=" ")
n=int(input("enter n:"))
displayprimes(n)
    
