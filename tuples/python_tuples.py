#Tuples

t = (10, 20, 30)
print(t)
print()

#creating a tuple
t = (1, 2, 3)
print(t)
print()

#without parenthesis
t = 1, 2, 3
print(t)
print()

#single element as a tuple
t = (5,)
print(t)
print(type(t))
print()

#Mixed Data Types
t = (10, "Python", True)
print(t)
print()

#Accessing Elements (Indexing)
t = (10, 20, 30, 40)

print(t[0])
print(t[2])
print(t[-1])
print()

#Tuple Slicing
t = (10, 20, 30, 40, 50)

print(t[1:4])
print(t[:3])
print(t[2:])
print(t[::-1])
print()

#Tuple is Immutable
t = (1, 2, 3)
# t[0] = 10    ERROR

#Concatenation
t1 = (1, 2)
t2 = (3, 4)

print(t1 + t2)
print()

#Repetition
t = (5, 6)
print(t * 3)
print()

#Membership Operators
t = (10, 20, 30)

print(20 in t)
print(5 not in t)
print()

#looping through a tuple
t = (10, 20, 30)

for x in t:
    print(x)
print()

#count
t = (1, 2, 2, 3)
print(t.count(2))
print()

#index
t = (10, 20, 30)
print(t.index(20))
print()

#Nested Tuples
t = ((1, 2), (3, 4))

print(t[0])
print(t[1][1])


