#Class Properties and Object Properties

#class properties

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("saivineeth", 22)

print(p1.name)
print(p1.age)
print()

#Access Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("saivineeth", 22)

print(p1.name) #accessing the properties
print(p1.age)
print()

#modifying properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("saivineeth", 22)

print(p1.name)
p1.age = 23
print(p1.age)
print()

#deleting properties
class Person:
  def __init__(self, name, age, course):
    self.name = name
    self.age = age
    self.course = course

p1 = Person("saivineeth", 22, "MCA")

print(p1.name)
print(p1.age)
del p1.course
#print(p1.course) #<- Shows an error
print()

#Class Properties vs Object Properties
class Student:
  course = "MCA"  #It is a class property

  def __init__(self, name, age):
    self.name = name    #instance properties
    self.age = age      #instance properties

std = Student("Saivineeth",22)

print(f"My name is {std.name}. I am studing in {std.course}")
print()

#Modifying Class Properties

class Student:
  course = "MCA"  #It is a class property

  def __init__(self, name, age):
    self.name = name    #instance properties
    self.age = age      #instance properties

std = Student("Saivineeth",22)

Student.course = "BCA" #modifying the class element

print(f"My name is {std.name}. I am studing in {std.course}")
print()