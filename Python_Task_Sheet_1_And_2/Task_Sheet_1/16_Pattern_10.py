# """
# *       *         *
#  *     * *     *   *
#   *   *   *   *   *
#    * *     * *     *
#     *       *       *
# """


n=int(input("Enter N : "))

count=1
count2=1

for i in range(n,0,-1):

    for s in range(1,count,1):
        print("-",end="")
    
    for j in range(1,i+1,1):
        if j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    count+=1

    
    
    for j in range(1,count2+1,1):
        if j==1 or j==count2:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    
    count2+=1
    print()