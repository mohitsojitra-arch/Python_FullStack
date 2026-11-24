#        1
#      2 3 2
#    3 4 5 4 3
#  4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5



num=int(input("Enter Number : "))

for i in range(1,num+1,1):

    for s in range(0,(num-i),1):
        print(" ",end=" ")
    
    count=i
    for j in range(1,i*2,1):
        if j<=i:
            print(count,end=" ")
            count+=1
        else:
            count-=1
            print(count,end=" ")

        if i==j:
            count-=1
    print()