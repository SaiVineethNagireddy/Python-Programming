"""Python operators
Operators are special symbols used to perform operations on variables and values."""

#Arthmetic operators
a = 10
b = 5

print(a + b)
print(a - b)
print(a % b)
print()

#Comparison (Relational) Operators
x = 5
print(x > 3)   # True
print(x == 5)  # True
print()

#Logical Operators
age = 20
print(age > 18 and age < 30)
print()

#Assignment operators
x = 10
x += 5
print(x)  #15
print()

#Bitwise Operators
a = 5   # 101
b = 3   # 011

print(a & b)  # 1
print(a | b)  # 7
print()

#Membership operator
numbers = [1, 2, 3]
names = ["sai", "Vineeth"]

print(2 in numbers)      # True
print(5 not in numbers)  # True
print("sai" in names)    # True
print()

#Identity operators
a = [1,2]
b = a
c = [1,2]

print(a is b)   # True
print(a is c)   # False

