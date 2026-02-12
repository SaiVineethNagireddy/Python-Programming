#sets

num = {1, 2, 3, 4}
print(num)
print()

#using setfunction
numbers = set([1, 2, 3, 4])
print(numbers)
print()

#Accessing the set elements
for i in numbers:
    print(i)
print()

#adding elements
numbers.add(5)
print(numbers)
print()

#update
numbers.update([6, 7, 8])
print(numbers)

#removing elements
#a.remove - it shows error if the element is not found
numbers.remove(8)
print(numbers)
print()

#b.discard - it does not show error if the element is not found
numbers.discard(8)
print(numbers)
print()

#pop() - Removes a random element
numbers.pop()
print(numbers)
print()

#clear() - Removes all the elements
numbers.clear()
print(numbers)