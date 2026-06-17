def findgcd(m,n):
    if n==0:
        return m
    else:
        r=n
        n=m%n        
        return findgcd(r,n)
m,n=map(int,input("enter m,n").split())
gcd=findgcd(m,n)
print(gcd)
