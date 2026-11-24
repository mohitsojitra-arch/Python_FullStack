list1 = list()

for i in range(0, 3, 1):
    temp_list = list()
    for j in range(0, 3, 1):
        num = int(input("Enter Number : "))
        temp_list.append(num)
    list1.append(temp_list)

print(list1)

determinant = (
    (list1[0][0] * ((list1[1][1] * list1[2][2]) - (list1[2][1] * list1[1][2])))
    - (list1[0][1] * ((list1[1][0] * list1[2][2]) - (list1[2][0] * list1[1][2])))
    + (list1[0][2] * ((list1[1][0] * list1[2][1]) - (list1[2][0] * list1[1][1])))
)

print(f"Determinant : {determinant}")
