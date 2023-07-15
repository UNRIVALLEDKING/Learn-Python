# Python Basics 🚀🔥

This code provides an introduction to the basics of Python programming. It covers fundamental concepts such as printing, indentation, variables, data types, and arithmetic operations. It also includes an exercise to practice variable assignment.

## Printing

Python's print statement is used to output text to the console. In Python 3, it is a function and should be invoked with parentheses.

```python
print("Yahallo!")
```

## Indentation

Python uses indentation to define code blocks instead of using curly braces. The standard indentation in Python is four spaces.

```python
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

print("Goodbye, World!")
```

## Variables and Types

Python is a dynamically-typed language, which means you do not need to declare variables before using them. Every variable in Python is an object.

```python
myint = 7
print(myint)
```

## Numbers

Python supports two types of numbers: integers and floating-point numbers.

```python
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
```

## Strings

Strings can be defined using either single quotes or double quotes. Double quotes allow for including apostrophes within the string.

```python
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)
```

## Assigning Multiple Variables

Assignments can be done on more than one variable "simultaneously" on the same line.

```python
a, b = 3, 4
print(a, b)
```

## Arithmetic Operations

Python supports arithmetic operations such as addition, subtraction, multiplication, and division.

```python
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
```

## Mixing Operators

Mixing operators between numbers and strings is not supported.

```python
# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)
```

## Exercise

The exercise in this code is about creating a string, an integer, and a floating-point number. The string should be named `mystring` and contain the word "Yahallo!". The floating-point number should be named `myfloat` and have the value 55.5. The integer should be named `myint` and have the value 80.

```python
# change this code
mystring = None
myfloat = None
myint = None

if mystring == "Yahallo!":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 55.5:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 80:
    print("Integer: %d" % myint)
```

By following this code documentation, you can grasp the fundamental concepts of Python and practice basic programming skills.
