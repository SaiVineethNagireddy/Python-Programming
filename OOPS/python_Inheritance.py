#inheritance

#parent class
class students:
    def __init__(self, initial, name):
        self.initial = initial
        self.name = name

    def fullname(self):
        print(f"fullname:{self.initial}.{self.name}")

std = students("nagireddy", "Saivineeth")
std.fullname()
print()

#creating a child class
class students:
    def __init__(self, initial, name):
        self.initial = initial
        self.name = name

    def fullname(self):
        print(f"fullname:{self.initial}.{self.name}")

class MCA(students):
    pass

std = MCA("nagireddy", "saivineeth")
std.fullname()
print()

#Add the __init__() Function
class myself:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"My name is {self.name} and i am {self.age} years old")

class course(myself):
    def __init__(self, name, age, course):
        super().__init__(name, age)

x = course("Saivineeth", 22, "MCA")
x.intro()