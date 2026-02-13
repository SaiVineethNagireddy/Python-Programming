#Private Properties
#In Python, you can make properties private by using a double underscore __ prefix:
class student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #private 

x = student("saivineeth", 22)
print(x.name)
#print(x.__age) #gives an error message

#using a method to access the value
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("saivineeth", 22)
print(p1.get_age())
print()

#To modify the private property
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("saivineeth", 22)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())
print()

#realtime Example
class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Saivineeth")
student.set_grade(86)
print(student.get_grade())
print(student.get_status())
print()

#Protected Properties
class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # Protected property

p1 = Person("Saivineeth", 5000)
print(p1.name)
print(p1._salary) # Can access, but shouldn't

#Private Methods
class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5) # This would cause an error

#Name Mangling
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("saivineeth", 22)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!