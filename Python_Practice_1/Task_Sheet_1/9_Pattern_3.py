# """
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# """


a=int(input("Enter Number : "))
i=1
num=1

while i<=a:
    j=1
    while j<=i:
        print(num,end=" ")
        num+=1
        j+=1
    print()    
    i+=1
    