#python Lists

lst = [1, 2, 3, 4]
print(lst)
print()

#Creating a list
a = [1, 2, 3]
b = ["Sai", "Vineeth"]
c = [1, "Python", True]
print(a)
print(b)
print(c)
print()

#Accessing the elements using the index values
a = [1, "Python", True]
b = [1, 2, 3]
c = ["Sai", "Vineeth"]

print(a[2])
print(b[-3])
print(c[1])
print()

#List Slicing
lst = [1, 2, 3, 4, 5, 6]
print(lst[1:4])
print(lst[:3])
print(lst[2:])
print(lst[::-1])
print()

#changing elements in a list
lst = [10, 200, 300]
lst[0] = 100
print(lst)
print()

#Adding elements to a list
#a.append
lst = [1, 2]
lst.append(3)
print(lst)
print()

#b.insert
lst = [1, 2, 3]
lst.insert(1,5)
print(lst)
print()

#c.extend()
a = [1, 2]
b = [4, 5]
a.extend(b)
print(a)
print()

#Removing elements in a list
#a.Remove
lst = [10, 20, 30]
lst.remove(20)
print(lst)
print()

#b.pop
lst = [10, 20, 3]
lst.pop()
print(lst)
print()

#c.del
lst = [1, 2, 3]
del lst[0]
print(lst)
print()

#d.clear()
lst = [1, 2, 3, 4, 5]
lst.clear()
print(lst)
print()

#List Length
lst = [1, 2, 3, 4]
print(len(lst))
print()

#sort
lst = [1,6,8,4,6,8,5,]
lst.sort()
print(lst)
print()

#reverse
lst = [5, 4, 3, 2, 1]
lst.reverse()
print(lst)
print()

#count
lst = [1, 3, 2, 4, 53, 2, 3, 45, 32, 34, 5, 3, 3]
print(lst.count(3))
print()

#index
lst = [1, 2, 3, 4]
print(lst.index(3))
print()

#copy
a = [1, 2, 3]
b = a.copy()
print(b)