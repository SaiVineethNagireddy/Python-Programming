#user input
name = input("Enter your name: ")
print("Hello", name)
print()

#input() always returns a string, even if you enter a number.
age = input("Enter age: ")
print(type(age))
print()

#Taking Integer Input
num = int(input("Enter number: "))
print(num * 2)
print()

#Taking Float Input
price = float(input("Enter price: "))
print(price + 10)
print()

#Taking Two Inputs in One Line
a, b = input("Enter the two numbers:").split()
print("a = ",a)
print("b = ",b)
print(type(a))  #str
print()

#Taking Two Integers in One Line
a, b = map(int, input("Enter two numbers:").split())
print("a = ",a)
print("b = ",b)
print()

#Taking List Input
numbers = list(map(int, input("Enter numbers: ").split()))
print("List:", numbers)
print("First element:", numbers[0])
print()

#Taking Character Input
ch = input("Enter a character: ")[0]
print("Character:", ch)
print()

