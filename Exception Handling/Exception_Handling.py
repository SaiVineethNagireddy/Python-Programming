#Exception handling in python

#print(10/0) which shows an zero division error


#using try and except
try:
    a = 10/0
except:
    print("some thing divided by zero is undefined")
print()

#multiple except blocks
try:
    a = int(input("Enter number: "))
    print(10 / a)
except ZeroDivisionError:
    print("Zero not allowed")
except ValueError:
    print("Invalid input")
print()

#using single except block
try:
    a = int(input("Enter number: "))
    print(10 / a)
except (ZeroDivisionError, ValueError) :
    print("Error occured")
print()

#
try:
    a = int(input("Enter number: "))
    print(10 / a)
except Exception as e:
    print("Error:", e)
print()

#using else block
try:
    a = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success")
print()

#finally
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")