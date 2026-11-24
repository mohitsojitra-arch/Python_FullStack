# """
# *******
# ***  ***
# **      **
# *          *
# **      **
# ***  ***
# *******
# """


num=int(input("Enter Number : "))

temp=1

for i in range(1,num*2,1):
    print("*",end=" ")

print()

for i in range(num-1,0,-1):
    for j in range(1,i+1,1):
        print("*",end=" ")

    for k in range(1,temp*2,1):
        print(" ",end=" ")

    for j in range(1,i+1,1):
        print("*",end=" ")

    print()
    temp+=1;

    
temp=num-1

for i in range(1,num,1):
    for j in range(1,i+1,1):
        print("*",end=" ")

    for k in range(1,temp*2,1):
        print(" ",end=" ")


    for p in range(1,i+1,1):
        print("*",end=" ")
    
    print()
    temp-=1


for i in range(1,num*2,1):
    print("*",end=" ")
