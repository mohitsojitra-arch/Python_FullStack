# """
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# """


a=int(input("Enter Number : "))
i=1

while i<=a:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()    
    i+=1
    