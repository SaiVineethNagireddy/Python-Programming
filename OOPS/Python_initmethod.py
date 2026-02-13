#__init__ method 
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#object
std = student("sai",22)

print(std.name)
print(std.age)
print()

#setting default value
class MCA:
    def __init__(self,name,age, course = "MCA"):
        self.name = name
        self.age = age
        self.course = course

std1 = MCA("seshagiri", 23, "MCA")
std2 = MCA("saivineeth", 22)

print(std1.name, std1.age, std1.course)
print(std2.name, std2.age, std2.course)
