list1=list()

size=int(input("Enter Size Of Circular Queue : "))
current_size=1


def FrontEnqueue():
    global current_size
    if current_size<=size:
        num=int(input(f"Enter Element (Front-Add) : {current_size}/{size}"))
        list1.insert(0,num)
        current_size+=1
    else:
        print("Circular Queue Is Overflow : ")


def RearEnqueue():
    global current_size
    if current_size<=size:
        num=int(input(f"Enter Element (Rear-Add) : {current_size}/{size}"))
        list1.append(num)
        current_size+=1
    else:
        print("Circular Queue Is Overflow : ")


def FrontDequeue():
    global current_size
    if current_size==1:
        print("Circular Queue Is Underflow : ")
    else:
        n=list1.pop(0)
        print(f"Front Dequeue : {n}")
        current_size-=1


def RearDequeue():
    global current_size
    if current_size==1:
        print("Circular Queue Is Underflow : ")
    else:
        n=list1.pop()
        print(f"Rear Dequeu : {n}")
        current_size-=1


def show():
    print(list1)

while 1:
    print("Choose Number \n 1 For FrontEnqueue \n 2 For RearEnqueue \n 3 For FrontDequeue \n 4 For RearDequeue \n 5 For Show \n 6 For Exit")
    user=int(input("Enter Option : "))

    if user==1:
        FrontEnqueue()
    elif user==2:
        RearEnqueue()
    elif user==3:
        FrontDequeue()
    elif user==4:
        RearDequeue()
    elif user==5:
        show()
    elif user==6:
        break 
    else:
        print("Enter Valid Option : ")
        
        