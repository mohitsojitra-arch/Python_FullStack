# A
# B B
# C C C
# D D D D
# E E E E E


num=int(input("Enter Number : "))

ch=65

for i in range(1,num+1,1):
    for j in range(1,i+1,1):
        print(chr(ch),end=" ")
    print()
    ch+=1
    