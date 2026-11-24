a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b      # True  (same values)
a is b      # False (two separate list objects in memory)
a is c      # True  (both point to the same list object)
a is not b  # True  (different objects in memory)


val1=5000
val2=5000

v1=250
v2=250

a1=5000
a2=a1

print(val1 is val2)
print(v1 is v2)
print(a1 is a2)
