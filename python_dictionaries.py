#Dictionaries

student = {
    "name" : "saivineeth",
    "age" : 22,
    "course" : "MCA"
}

print(student)
print(student["age"])
print(student.get("name"))
print()

#Modifying a Dictionary
student["age"] = 21           #update
student["city"] = "Hyderabad" #helps you to add the new key
print(student)
print()

#removing elements
student.pop("age")
print(student)

del student["city"]
print(student)

student.clear()

print(student)
print()

#Dictionary Methods

student = {
    "name" : "saivineeth",
    "age" : 21,
    "course" : "MCA"
}

#keys
print(student.keys())
print()

#values
print(student.values())
print()

#items
print(student.items())
print()

#update
student.update({"age" :22})
print(student)
print()

#pop
student.popitem()
print(student)
print()

#looping through a dictionary

student = {
    "name" : "saivineeth",
    "age" : 21,
    "course" : "MCA"
}

for key in student:
    print(key)
print()

for value in student.values():
    print(value)
print()

for key, value in student.items():
    print(key, value)
print()


#Nested Dictionaries

students = {
    "s1": {"name": "Ravi", "age": 22},
    "s2": {"name": "sai", "age": 23}
}

print(students)
print(students["s1"])
print(students["s2"]["name"])
print()

