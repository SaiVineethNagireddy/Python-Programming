#looping Statements

#for loop
#looping a list
fruits = ["apple", "banana", "cherry"]

for i in fruits:
    print(i)
print()

#Using range() - range(start, stop, step)
for i in range(6):
    print(i)
print()

for i in range(2, 10, 2):
    print(i)
print()


#looping a string
a = "Python"
for i in a:
    print(i)
print()

#looping thorugh a dictionary
a = {"course" : "python", "price" : 1000}
for i, j in a.items():
    print(i, j)
print()

#Using else with loops
for i in range(3):
    print(i)
else:
    print("Loop finished successfully")
print()

#1.1 Nested loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i,j)
print()

#2.While loop
i = 1

while i <= 5:
    print(i)
    i += 1
print()

#real time example using nested for loop
for i in range(1,2):
    for j in range(1, 11):
        print(i , "*" , j ,"=", (i *j))
print()