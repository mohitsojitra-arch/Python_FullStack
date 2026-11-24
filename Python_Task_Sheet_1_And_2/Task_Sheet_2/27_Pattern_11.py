# 1 2 3 4
# 12 13 14 5
# 11 16 15 6
# 10 9 8 7


n = int(input("Enter Number: "))

arr = [[0 for j in range(n)] for i in range(n)]

top = 0
bottom = n - 1
left = 0
right = n - 1

num = 1

while num <= n * n:

    # 1. Left to Right
    for j in range(left, right + 1):
        arr[top][j] = num
        num += 1

    top += 1

    # 2. Top to Bottom
    for i in range(top, bottom + 1):
        arr[i][right] = num
        num += 1

    right -= 1

    # 3. Right to Left
    for j in range(right, left - 1, -1):
        arr[bottom][j] = num
        num += 1

    bottom -= 1

    # 4. Bottom to Top
    for i in range(bottom, top - 1, -1):
        arr[i][left] = num
        num += 1

    left += 1


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")

    print()
