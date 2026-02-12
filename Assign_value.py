"""Variables
variables are containers for storing data values
The variable names ar case sensitive"""

a = "SaiVineeth"
b = 10.0

print("the name is", a)
print(b)
print()

#Type casting

c = int(1.00)
d = str(10.1)
e = float(1)
print(c); print(d); print(e)
print()

#Get the type of the variable
print(type(c))
print(type(d))
print(type(e))
print()

#Multiple variables
x, y, z = "sai", "Vineeth", "Nagireddy"
print(x)
print(y)
print(z)
print()

x = y = z = "Same"
print(x)
print(y)
print(z)
print()


#unpacking a collection
#list
MCA = ["sai", "Sesh", "jagadeesh", "Teja", "chenna", "mani"]
a, b, c,d, e, f = MCA
print(a, b, c, d, e, f)
print()

#printing a variable
a = 10
b = "Hello"
print(a, b)
print()

#Global Variable

x = "awesome"

def myfunc() :
    x = "Beginner Friendly"
    print("python is", x)#python is beginner friendly

myfunc()

print("python is", x)#python is awesome
print()


#using global keyword
a = "Average"

def myfun():
    global a  #This is used to define variable and we can access outside of the function
    a = "Nice"

myfun()

print("Python is", a)#python is nice