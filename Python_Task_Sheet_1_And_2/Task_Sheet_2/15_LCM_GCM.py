
a = int(input("Enter Value 1 : "))
b = int(input("Enter Value 2 : "))

big = 0
small = 0


if a > b:
    big = a
else:
    big = b

# LCM
while 1:
    if big % a == 0 and big % b == 0:
        print(f"LCM : {big}")
        break
    else:
        big += 1

if a > b:
    small = b
else:
    small = a


# GCD
for i in range(1, small + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(f"GCD : {gcd}")
