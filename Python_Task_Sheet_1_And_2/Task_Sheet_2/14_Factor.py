fac=int(input("Enter Number : "))

print("Factors : ")

for i in range(1,(fac+1),1):
    if fac%i==0:
        print(i)