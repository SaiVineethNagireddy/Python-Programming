#Conditional statements

# if statements
age = 18
if age >= 18:
    print("You are elgible to vote")
print()

#if else statements

age = 10

if age >= 18:
    print("Major")
else:
    print("Minor")
print()

#if-elif-else

marks = 86

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
print()

#Nested if statements
age = 21
citizen = True

if age >= 18:
    if citizen:
        print("You are eligible to vote")
print()

#using logical operators
age = 25

if age > 18 and age < 30:
    print("Young adult")
print()

x = 10

if x == 10:
    print("Equal")
print()

#ternary condition 
age = 17
Status = "Adult" if age >= 18 else "minor"
print(Status)

