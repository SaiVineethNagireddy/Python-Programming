 Python Programming

  Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:
    web development
    software development
    system scripting
    AI & ML
    Data Analytics etc..

1.Basic print Statement
    print("Hello, World!")

Python is an interpreted programming language. We save python file using .py Extension. To run the file we type "python intro.py"

2.Python Indentation
    Indentation refers to the spaces at the beginning of a code line.Indentation in Python is very important.The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

3.python comments
    Comments can be used to explain Python code.Comments can be used to make the code more readable.

        a. single line comments
            Comments starts with a '#'
                #This is a comment
                print("Hello, World!")
        b.Multiline comments
            for multiline comments we use triple quotes
                """This is a 
                Multiline comment"""

3.Variables
    Variables are containers for storing data values.
        x = 5
        print(x)

        x is the variable name
        = means “store this value”
        5 is the value
    
    a.Variable Names (Rules to be followed)
        A variable name must start with a letter or the underscore character.
        A variable name cannot start with a number.
        A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
        Variable names are case-sensitive (age, Age and AGE are three different variables).
        A variable name cannot be any of the Python keywords.

4.DataTypes
    In programming, data type is an important concept.
    Variables can store data of different types, and different types can do different things.
    Python has the following data types built-in by default, in these categories:
            Text Type:	    str
            Numeric Types:	int, float, complex
            Sequence Types:	list, tuple, range
            Mapping Type:	dict
            Set Types:	    set, frozenset
            Boolean Type:	bool
            Binary Types:	bytes, bytearray, memoryview
            None Type:	    NoneType

    Example:x = 5
            print(type(x))

x = "Hello World"	                            str	
x = 20	                                        int	
x = 20.5	                                    float	
x = 1j	                                        complex	
x = ["apple", "banana", "cherry"]	            list	
x = ("apple", "banana", "cherry")	            tuple	
x = range(6)	                                range	
x = {"name" : "John", "age" : 36}	            dict	
x = {"apple", "banana", "cherry"}	            set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	                                    bool

5.Type Conversion
    You can convert from one type to another 
    Example:x = 5
            a = float(x)

6.python Strings
    A string is a sequence of characters (letters, numbers, symbols) enclosed in quotes.
    Example: a = "hello"

        a.String methods
            lower() – Converts all characters to lowercase.
            upper() – Converts all characters to uppercase.
            title() – Converts first letter of each word to uppercase.
            capitalize() – Capitalizes only the first character of the string.
            strip() – Removes spaces from both beginning and end.
            lstrip() – Removes spaces from the left side only.
            rstrip() – Removes spaces from the right side only.
            replace(old, new) – Replaces one part of the string with another.
            find(text) – Returns the position of the first occurrence of text.
            count(text) – Counts how many times text appears.
            startswith(text) – Checks if the string starts with given text.
            endswith(text) – Checks if the string ends with given text.
            split() – Splits the string into a list.
            join() – Joins elements of a list into one string.
            isalpha() – Checks if all characters are letters.
            isdigit() – Checks if all characters are numbers.
            isalnum() – Checks if all characters are letters and numbers.

7.operators
    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators

            a.Arithmetic operators
                Used for mathematical calculations.
                    a = 10
                    b = 3
                    print(a + b)
                    print(a // b)
                    print(a % b)
                    print(a ** b)

            b.Comparision Operator
                Return True or False.
                    x = 5
                    print(x > 3)   # True
                    print(x == 5)  # True

            c.Logical Operators
                Used with Boolean values.
                    age = 20
                    print(age > 18 and age < 30)

            d.Assignment Operators
                used to assign the values
                    x = 10
                    x += 5
                    print(x)

            e.Bitwise Operators
                Works on binary numbers
                    a = 5   # 101
                    b = 3   # 011

                    print(a & b)  # 1
                    print(a | b)  # 7

            f.Membership Operators
                in and not in. in - if value exist where as not in - value does not exist
                    numbers = [1, 2, 3]
                    print(2 in numbers)      # True
                    print(5 not in numbers)  # True

            g.Identity operators
                is and is not . is - if it is same object where as is not - not the same object
                    a = [1,2]
                    b = a
                    c = [1,2]

                    print(a is b)   # True
                    print(a is c)   # False

8.conditional statements
    Conditional statements allow your program to make decisions.They execute certain blocks of code only if a condition is True.

    a.if condition
        age = 18
        if age >= 18:
            print("You are eligible to vote.")

    b.The if-else Statement
        number = 5
        if number % 2 == 0:
            print("Even")
        else:
            print("Odd")

    c.The if-elif-else Statement
        marks = 86
        if marks >= 90:
            print("Grade A")
        elif marks >= 75:
            print("Grade B")
        elif marks >= 50:
            print("Grade C")
        else:
            print("Fail")

    d.Nested if Statements
        age = 20
        citizen = True
        if age >= 18:
            if citizen:
                print("Eligible to vote")

9.Looping Statements
    a.for Loop
        Used to iterate over a sequence (list, tuple, string, dictionary, range, etc.)
            Basic Syntax:
                for variable in sequence:
                # code block

    b.The while Loop
        Used when you don’t know how many times to loop.
            Syntax
                while condition:
                # code block

    c.break Statement
        Stops the loop immediately.
            for i in range(10):
            if i == 5:
                break
            print(i)

    d.continue Statement
        Skips current iteration.
            for i in range(5):
            if i == 2:
                continue
            print(i)

    e.Nested Loops
        Loop inside another loop.
            for i in range(1, 4):
            for j in range(1, 4):
                print(i, j)

10.match-case
    It is switch case alternative
        day = 2
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case _:
                print("Invalid day")

11.Lists
    A list is a collection data type in Python that:
            Is ordered
            Is mutable (changeable)
            Allows duplicate values
            Can store different data types

        my_list = [10, 20, 30, 40]
        print(my_list)

    a.List methods
        append(), insert(), remove(), pop(),
sort(), reverse(), extend()

12.Tuples
    A tuple is a collection of items that is:
        Ordered
        Immutable (cannot change)
        Allows duplicates

    t = (10, 20, 30)
    print(t)

13.dictionary
    every thing about dictionaries
    Word = Key
    Meaning = Value
        Example:
            student = {
            "name": "Ravi",
            "age": 20,
            "course": "Python"
        }

14.sets
    A set is a built-in data type used to store multiple unique items.
        No duplicates
        Unordered
        No indexing
            Example: numbers = {1, 2, 3, 4}

15.python JSON
    JSON in Python is a module used to convert Python objects to JSON format and convert JSON data back into Python objects.We import the "import json"
    
16.math functions
    The math module is a built-in Python module that provides mathematical functions and constants like square root, power, trigonometry, logarithms, etc. We have to "import math".

17. Exception Handling
    When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
    **Why Exception Handling is Important
    Prevents program crash
    Handles runtime errors gracefully
    Maintains program flow
    Provides meaningful error messages
    Improves reliability

    a.Try Except
        The try block lets you test a block of code for errors.
        The except block lets you handle the error.
        The else block lets you execute code when there is no error.
        The finally block lets you execute code, regardless of the result of the try- and except blocks.

18.User_Input
    User input means taking data from the user during program execution. In Python, we use the input() function to get input from the user.
        name = input("Enter your name: ")
        print("Hello", name)

19.File-Handling
    File handling allows us to:
        Create files
        Read files
        Write files
        Append data
        Delete files
    Python provides built-in open() function for file operations.

Object Oriented programming
    OOP stands for Object-Oriented Programming.Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

Advantages of OOP:
    Provides a clear structure to programs
    Makes code easier to maintain, reuse, and debug
    Helps keep your code DRY (Don't Repeat Yourself)
    Allows you to build reusable applications with less code

Classes and Objects:
    Classes and objects are the two core concepts in object-oriented programming.
      A class defines what an object should look like, and an object is created based on that class. For example:
        Class	 Objects
        Fruit  - Apple, Banana, Mango
        Car	   - Volvo, Audi, Toyota

Python __init__() Method:
    All classes have a built-in method called __init__(), which is always executed when the class is being initiated.The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

The self Parameter:
    The self parameter is a reference to the current instance of the class.It is used to access properties and methods that belong to the class.

Python Class Properties:
    Properties are variables that belong to a class. They store data for each object created from the class.
    Example:
            class Person:
                def __init__(self, name, age):
                    self.name = name
                    self.age = age

                p1 = Person("Emil", 36)

                print(p1.name)
                print(p1.age)

Python Class Methods:
    Methods are functions that belong to a class. They define the behavior of objects created from the class.
    Example: 
            class Person:
                def __init__(self, name):
                    self.name = name

                def greet(self):
                    print("Hello, my name is " + self.name)

                p1 = Person("sai")
                p1.greet()

Python Inheritance:
    Inheritance allows us to define a class that inherits all the methods and properties from another class.    
    Parent class is the class being inherited from, also called base class.
    Child class is the class that inherits from another class, also called derived class.

Python Polymorphism:
    The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

Python Encapsulation
    Encapsulation is about protecting data inside a class.
    It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
    This prevents accidental changes to your data and hides the internal details of how your class works.
