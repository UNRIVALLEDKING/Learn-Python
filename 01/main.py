# Explanation of the Python code

'''
Python is a very simple language, and has a very straightforward syntax. It encourages programmers to program without boilerplate (prepared) code. The simplest directive in Python is the "print" directive - it simply prints out a line (and also includes a newline, unlike in C).

There are two major Python versions, Python 2 and Python 3. Python 2 and 3 are quite different. This tutorial uses Python 3 because it is more semantically correct and supports newer features.

For example, one difference between Python 2 and 3 is the print statement. In Python 2, the "print" statement is not a function, and therefore it is invoked without parentheses. However, in Python 3, it is a function and must be invoked with parentheses.
'''

print("Yahallo!")  # Prints "Yahallo!" to the console


'''
Indentation
Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported, but the standard indentation requires standard Python code to use four spaces. For example:
'''
x = 4
if x == 4:
    # indented four spaces
    print("x is 4.")


print("Goodbye, World!")  # Prints "Goodbye, World!" to the console


'''
Variables and Types
Python is completely object-oriented, and not "statically typed". You do not need to declare variables before using them or declare their type. Every variable in Python is an object.
'''

myint = 7  # Assigns the integer value 7 to the variable myint
print(myint)  # Prints the value of myint


'''
Numbers
Python supports two types of numbers - integers (whole numbers) and floating-point numbers (decimals). It also supports complex numbers.
'''
myfloat = 7.0  # Assigns the floating-point value 7.0 to the variable myfloat
print(myfloat)  # Prints the value of myfloat
myfloat = float(7)  # Converts the integer 7 to a floating-point number and assigns it to myfloat
print(myfloat)  # Prints the value of myfloat


'''
Strings
Strings are defined either with single quotes or double quotes. The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes).
'''
mystring = 'hello'  # Assigns the string "hello" to the variable mystring
print(mystring)  # Prints the value of mystring
mystring = "hello"  # Assigns the string "hello" to the variable mystring
print(mystring)  # Prints the value of mystring
mystring = "Don't worry about apostrophes"  # Assigns the string "Don't worry about apostrophes" to the variable mystring
print(mystring)  # Prints the value of mystring


one = 1  # Assigns the integer value 1 to the variable one
two = 2  # Assigns the integer value 2 to the variable two
three = one + two  # Adds the values of one and two, and assigns the result to the variable three
print(three)  # Prints the value of three


hello = "hello"  # Assigns the string "hello" to the variable hello
world = "world"  # Assigns the string "world" to the variable world
helloworld = hello + " " + world  # Concatenates the values of hello, a space, and world, and assigns the result to helloworld
print(helloworld)  # Prints the value of helloworld


a, b = 3, 4  # Assigns the values 3 and 4 to the variables a and b simultaneously
print(a, b)  # Prints the values of a and b


'''
Mixing operators between numbers and strings is not supported:
'''
# The following line of code will raise a TypeError since it tries to add an integer, a string, and another integer
# print(one + two + hello)


# Solution to the exercise

mystring = "Yahallo!"  # Assigns the string "Yahallo!" to the variable mystring
myfloat = 55.5  # Assigns the floating-point value 55.5 to the variable myfloat
myint = 80  # Assigns the integer value 80 to the variable myint

if mystring == "Yahallo!":
    print("String: %s" % mystring)  # Prints the value of mystring
if isinstance(myfloat, float) and myfloat == 55.5:
    print("Float: %f" % myfloat)  # Prints the value of myfloat
if isinstance(myint, int) and myint == 80:
    print("Integer: %d" % myint)  # Prints the value of myint
