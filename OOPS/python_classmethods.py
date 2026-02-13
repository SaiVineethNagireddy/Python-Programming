#Python Class Methods

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(a):
        print(f"Hello my name is {a.name} and i am {a.age} years old")

std1 = student("vineeth",23)
std1.intro()
print()

#Methods with parameters

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))
print()

#Methods Accessing Properties
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(a):
        print(f"Hello my name is {a.name} and i am {a.age} years old")

std1 = student("vineeth",23)
std1.intro()
print()

#Methods Modifying Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("sai", 22)
p1.celebrate_birthday()
p1.celebrate_birthday()
print()

#The __str__() method

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

s1 = Student("Sai", 21)
print(s1)
print()

#Multiple methods
class MCA:
    def __init__(self, names):
      self.names = names
      self.students = []

    def add_student(self, students):
      self.students.append(students)
      print(f"student added : {self.students}")
    
    def remove_student(self, students):
       self.students.remove(students)
       print(f"student Removed: {self.students}")

    def MCA_students(self):
       print(f"MCA Students : {self.names}")
       for student in self.students:
          print(f"{student}")

course = MCA("MCA")
course.add_student("Saivineeth")
course.add_student("narshima")
course.remove_student("narshima")
course.MCA_students()
print()

#Delete Methods
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello!")

p1 = Person("saivineeth")
del Person.greet
p1.greet() #This shows an error