
list1 = list()
list2 = list()

for i in range(1, 4):
    temp_list = list()

    for j in range(1, 4):
        num = int(input(f"Enter Number [{i}][{j}]: "))
        temp_list.append(num)

    list1.append(temp_list)

print("First Matrix:", list1)


for i in range(1, 4):
    temp_list = list()

    for j in range(1, 4):
        num = int(input(f"Enter Number [{i}][{j}]: "))
        temp_list.append(num)

    list2.append(temp_list)

print("Second Matrix:", list2)


ans = list()

for i in range(0, 3):
    temp_list = list()

    for j in range(0, 3):
        current_sum = 0

        for k in range(0, 3):
            current_sum += list1[i][k] * list2[k][j]

        temp_list.append(current_sum)

    ans.append(temp_list)

print("Multiplication:", ans)