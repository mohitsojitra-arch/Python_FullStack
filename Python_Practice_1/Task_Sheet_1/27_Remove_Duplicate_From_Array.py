list1=[10,20,20,10,40,30,50,10,30,60,40,50,60]

print(list1)
set1=set(list1)
print(set1)

list2=[]

for i in list1:
    if i in list2:
        continue
    else:
        list2.append(i)

print(list2)