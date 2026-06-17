def push(x):
    l.append(x)
def pop():
    if len(l)==0:
        return -1
    return l.pop()
def peek():
    if len(l)==0:
        return -1
    return l[-1]     
l=[]
print("Stack using list")
while(True):
    print("1.for push\n 2.for pop \n 3.for peek element \n 4.print elements\n5.exit")
    ch=int(input())
    match(ch):
        case 1:
            print("enter value")
            x=int(input())
            push(x)
        case 2:
            print(pop())
        case 3:
            print(peek())
        case 4:
            print(l)
        case 5:break
        case _:print("invalid")
    
    
    
    
    
