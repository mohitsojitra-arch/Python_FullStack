#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     * 


num=int(input("Enter Number : "))

for i in range(1,num+1,1):

    for s in range(0,num-i,1):
        print(" ",end="")
    
    for j in range(1,(i+1),1):
        print("*",end=" ")
        
    print()

for i in range(num-1,0,-1):

    for s in range(0,num-i,1):
        print(" ",end="")
    
    for j in range(1,(i+1),1):
        print("*",end=" ")
    print()

