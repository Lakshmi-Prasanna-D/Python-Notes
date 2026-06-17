'''
a=int(input("enter n"))
verify=lambda x: "positive" if x>0 else "negative"  if x<0 else "zero"
print(verify(a))
'''
a,b=map(int,input("enter a,b\n").split())
add=lambda x,y: x+y
product=lambda x,y: x*y
quotient=lambda x,y:x//y if y!=0 else "invalid"
remainder =lambda x,y:x%y if y!=0 else "invalid"
print("sum:",add(a,b))
print("product:",product(a,b))
print("quotient:",quotient(a,b))
print("remainder:",remainder(a,b))

