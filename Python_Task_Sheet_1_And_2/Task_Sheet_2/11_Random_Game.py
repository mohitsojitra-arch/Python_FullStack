import random

ran=str(random.randint(1000,9999))
list1=list()

print(ran)

while 1:
    num=input("Enter Guess Number : ")
    
    if num==ran:
        print("Correct : ")
        print(list1)
        break
    else:
        for i in range(0,4,1):
            if(ran[i]==num[i]):
                print("Cow",end="-")
            else:
                print("Bull",end="-")
        print()
        list1.append(num)