def push(x):
    l.append(x)
def pop():
    if len(l)==0:
        return -1
    return l.pop(0)
def front():
    if len(l)==0:
        return -1
    return l[0]
def rear():
    if len(l)==0:
        return -1;
    return l[-1]
l=[]
print("Queue using List\n")
while(True):
    print("1.for enqueue\n 2.for dequeue \n 3.for front element\n 4.last element\n 5.print elements\n6.exit")
    ch=int(input())
    match(ch):
        case 1:
            print("enter value")
            x=int(input())
            push(x)
        case 2:
            print(pop())
        case 3:
            print(front())
        case 4:
            print(rear())
        case 5:
            print(l)
        case 6:break
        case _:print("invalid")
    
    
    
    
    
