# """
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# """


a=int(input("Enter Number : "))

while a>=1:
    j=a 
    while j>=1:
        print(j,end=" ")
        j-=1
    print()
    a-=1
    