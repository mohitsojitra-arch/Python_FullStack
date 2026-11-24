list1=list()
size=int(input("Enter Queue Size : "))
current_size=1

def enqueue():
    global current_size
    global size
    if  current_size<=size:
        num=int(input(f"Enter Element : {current_size}/{size}"))
        list1.append(num)
        current_size+=1
    else:
        print("Queue Overflow : ")


def dequeue():
    global current_size
    global size
    if current_size==1:
        print("Queue in Underflow : ")
    else:
        ele=list1.pop(0)
        current_size-=1
        print(f"Dequeue Element : {ele}")
        

def show():
    print(list1)


def peek():
    if current_size==1:
        print("Queue Is Underflow")
    else:
        print(f"Peek Element :{list1[0]}")



while 1:
    print("Choose Option \n 1 For Enqueue \n 2 For Dequeue \n 3 For Show \n 4 For Peek \n 5 For Exit")
    num=int(input("Enter Number : "))

    if num == 1:
        enqueue()
    elif num==2:
        dequeue()
    elif num==3:
        show()
    elif num==4:
        peek()
    elif num==5:
        break
    