"""Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.
String is IMMUTABLE"""
x = "Sai"
print("Hello", x)
print()

#writing multiple line text to a variable
x = """Hello this is a multiline Text
I am Revising python programming
I like to learn coding"""
print(x)
print()

#Accessing the elements(Characters) in a string
#INDEXING
c = "Saivineeth"
print(c[0])  #S
print(c[-1]) #h
print()

#SLICING Format(String[start: stop: step])
print(c[0:4]) #saiv
print(c[2:])  #ivineeth
print(c[:3])  #sai
print(c[::-1])#hteenivias (Reverse)
print()

#Concentenation
a = "Hello"
b = "World"

print(a + "!" + b) #Hello!World
print(a * 3)#HelloHelloHello
print()

#Using len to find the length of the string
a = "Python Programming"
print(len(a)) #18
print()

#Using Membership Operator(in and not in)
a = "Python Programming"
print("python" in a)   #True
print("java" not in a) #False
print()

#Case Conversion methods
a = "PYTHON"
print(a.lower())       #python
print(a.upper())       #PYTHON
print(a.title())       #Python
print(a.capitalize())  #Python
print(a.swapcase())    #pYtHoN
print()

#Removing spaces using strip
a = "     Hello      "
print(a.strip())  #Hello
print(a.lstrip()) #"Hello   "
print(a.rstrip()) #"   Hello"
print()

#Searching and counting in a string
a = "python Programming"
print(a.find("th")) #2(index value)
print(a.rfind("mm")) #13(Shows the right most position)
print(a.count("m"))  #2(no of times repeated)
print()

#Replace
a = "I am learning java"
print(a.replace("java", "python")) # I am learning python
print()

#split and join
a = "10,02,2026"

seperate = a.split(",") 
print(seperate)           #['10', '01', '2026']
print()

date = "-".join(seperate)
print(date)               #10-01-2026
print()

#Looping through strings to get each character
a = "LoopME"
for i in a :
    print(i)
print()

#String Method Checking
print("Python".isalpha())     #True
print("123".isdigit())        #True
print("Python123".isalnum())  #True
print("hello".islower())      #True
print("HELLO".isupper())      #True
print()

#String Formatting
name = "saivineeth"
age = 22
percentage = 86.910
print(f"My name is {name}. I am {age} years old")
print(f"My percentage is {percentage: .2f}")
print()
