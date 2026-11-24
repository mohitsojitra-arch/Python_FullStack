#     1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
#  1 5 10 10 5 1


num = int(input("Enter Number of Rows: "))

lst = []

for i in range(num):

    row = []

    for j in range(i + 1):

        if j == 0 or j == i:
            row.append(1)

        else:
            value = lst[i-1][j-1] + lst[i-1][j]
            row.append(value)

    lst.append(row)


print(lst)
print(len(lst[0]))
print(len(lst[1]))
print(len(lst[2]))
print(len(lst[3]))

for i in range(num):
    print(" " * (num-i), end="")

    for j in range(i+1):
        print(lst[i][j], end=" ")
    print()
