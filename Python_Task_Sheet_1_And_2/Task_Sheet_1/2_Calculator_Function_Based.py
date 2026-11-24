def My_Calculator():
    a=int(input("Enter Value 1 : "))
    b=int(input("Enter Value 1 : "))
    
    print("Enter Operation sign \n 1 for + \n 2 for - \n 3 for * \n 4 for / \n 5 for % \n 6 for ** \n 7 for //")
    opr=int(input("Enter Operation Sign Number: "))
    
    if opr==1:
        print(f"{a} + {b} = {a+b}")
    elif opr == 2:
        print(f"{a} - {b} = {a-b}")
    elif opr == 3:
        print(f"{a} * {b} = {a*b}")
    elif opr == 4:
        print(f"{a} / {b} = {a/b}")
    elif opr == 5:
        print(f"{a} % {b} = {a%b}")
    elif opr == 6 :
        print(f"{a} ** {b} = {a**b}")
    elif opr == 7:
        print(f"{a} // {b} = {a//b}")
    else:
        print("Enter Valid Sign : ")


My_Calculator()
    