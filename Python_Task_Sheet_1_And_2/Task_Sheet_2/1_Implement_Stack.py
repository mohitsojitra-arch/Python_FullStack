stack=list()
current_count=1

def push():
   global current_count
   if current_count<=count: 
    num=int(input(f"Enter Stack Element :  {current_count}/{count}"))
    current_count+=1
    stack.append(num)
   else:
     print("Stack Is Overflow : ")

def pop():
    global current_count
    if current_count==1:
        print("Stack Is Underflow (Empty) : ")
    else:
        stack.pop()
        current_count-=1
        print("POP Element : ")

def show():
    print(stack)

def peek():
    if current_count == 1:
        print("Stack Is Underflow (Empty) : ")
    else:
        print(stack[len(stack)-1])

        

count=int(input("Enter Stack Size : "))

while 1:
    print("1 For PUSH() \n 2 For POP() \n 3 For SHOW() \n 4 For PEEK() \n 5 For Exit")
    user=int(input("Enter Option : "))

    if user == 1:
     push()
    elif user == 2:
     pop()
    elif user == 3:
     show()
    elif user == 4:
      peek()
    elif user == 5:
        break
    else:
        print("Enter Valid Option : ")
