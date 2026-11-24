#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *


num=int(input("Enter Number : "))

for i in range(1,num+1,1):

    for s in range(0,(num-i),1):
        print("  ",end="")
    
    for j in range(0,(i*2)-1,1):
        print("*",end=" ")
    print()