#File handling in python

#Method - 1
file = open("example.txt", "r")
data = file.read()
print(data)
file.close()
print()

"""This is regarding python
The topic is regarding the file handling"""

#Method-2
file = open("example.txt","r")
data = file.readline()
print(data)
file.close()
print()

"""This is regarding python"""

#method-3
file = open("example.txt", "r")
data = file.readlines()
print(data)
file.close()
print()

"""['This is regarding python\n', 'The topic is regarding the file handling']"""

#Writing a file
file = open("examples.txt", "w")    #this creates a new file to write or if the file exist it rewrites the text
file.write("I am adding text to the file using write")
file.close()

#lets read the file to check if it is added
file = open("examples.txt", "r")
data = file.read()
print(data)
file.close()
print()

#using append
file = open("examples.txt", "a")    
file.write("\n appending text using append \'a\'")
file.close()

#using "x"
#it creates new file. If the file exist it shows error
file = open("newfile.txt", "x")
file.write("New file created")
file.close()

