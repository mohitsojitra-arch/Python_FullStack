matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


def show_matrix():
    print("************************")
    for i in range(0,3,1):
        for j in range(0,3,1):
            print(matrix[i][j],end=" ")
        print()
    print("************************")

def change_matrix(index,sign):
     global matrix
     for i in range(0,3,1):
        for j in range(0,3,1):
            if(index==matrix[i][j]):
                matrix[i][j]=sign


# Row Check Matrix
def check_1(sign):
    for i in range(0,3,1):
        temp=0
        for j in range(0,3,1):
            if matrix[i][j] == sign:
                temp+=1
            
        if temp==3:
            return 1

# Column Check Martix
def check_2(sign):
    for i in range(0,3,1):
        temp=0
        for j in range(0,3,1):
            if matrix[j][i] == sign:
                temp+=1
            
        if temp==3:
            return 1

# Diagonal Element Check Matrix
def check_3(sign):
    temp=0
    for i in range(0,3,1):
        for j in range(0,3,1):
            if matrix[i][j] == sign and i==j:
                temp+=1
            
        if temp==3:
            return 1


# Anti Diagonal Element Check Matrix
def check_3(sign):
    temp=0
    for i in range(0,3,1):
        for j in range(0,3,1):
            if matrix[i][j] == sign and i+j==2:
                temp+=1
            
        if temp==3:
            return 1

count=0
while 1:
    print("-------------------")
    print(f"Player {"1" if count%2==0 else "2" } Sign {"O" if count%2==0 else "X" } ")
    print("Enter Index Number :")
    print("-------------------")
    print(f"Enter Index Number : ")
    show_matrix()
    user_index=int(input())
    sign="O" if count%2==0 else "X"
    change_matrix(user_index,sign)
    show_matrix()
    if check_1(sign) == 1:
        print(f"Winner : Player {"1" if count%2==0 else "2" }")
        break
    if check_2(sign) == 1:
        print(f"Winner : Player {"1" if count%2==0 else "2" }")
        break
    if check_3(sign) == 1:
        print(f"Winner : Player {"1" if count%2==0 else "2" }")
        break
    count+=1
