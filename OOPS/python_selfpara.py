#python self parameter
 
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"Hello my name is {self.name} and i am {self.age} years old")

std = student("sai",22)
std.intro()
print()

#self Does Not Have to Be Named "self"
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(a):
        print(f"Hello my name is {a.name} and i am {a.age} years old")

std1 = student("vineeth",23)
std1.intro()
print()

#Calling Methods with self

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(a):
    message = a.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Saivineeth")
p1.welcome()