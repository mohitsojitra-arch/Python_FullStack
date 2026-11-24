# """
# 10 9 8 7
# 6 5 4
# 3 2
# 1
# """


a=int(input("Enter Number : "))

count=sum(range(1,a+1,1))
print(count)

while a>=1:
   j=1
   while j<=a:
       print(count,end=" ")
       count-=1
       j+=1
   print()    
   a-=1    