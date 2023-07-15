# Python Basics Documentation 🚀🔥

This documentation provides a comprehensive introduction to the basics of Python programming. It covers essential concepts such as printing, indentation, variables, data types, arithmetic operations, and more. By following this documentation, beginners can acquire a solid foundation in Python programming and develop their skills progressively.

## Table of Contents

- [Printing](#printing)
- [Indentation](#indentation)
- [Variables and Types](#variables-and-types)
- [Numbers](#numbers)
- [Strings](#strings)
- [Assigning Multiple Variables](#assigning-multiple-variables)
- [Arithmetic Operations](#arithmetic-operations)
- [Mixing Operators](#mixing-operators)
- [Exercise](#exercise)

## Printing <a name="printing"></a>

Printing is a fundamental operation in Python that outputs text or data to the console. The `print()` function is used for this purpose. In Python 3, it is invoked as a function and should be enclosed in parentheses.

```python
print("Yahallo!")
```

The above code prints the text "Yahallo!" to the console.

## Indentation <a name="indentation"></a>

Python uses indentation to define code blocks instead of using curly braces like some other programming languages. The standard convention in Python is to use four spaces for indentation.

```python
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

print("Goodbye, World!")
```

In the above code, the indentation is used to indicate that the `print("x is 1.")` statement is part of the if block.

## Variables and Types <a name="variables-and-types"></a>

Python is a dynamically-typed language, meaning you don't need to declare variables explicitly before using them. Variables are created when you assign a value to them.

```python
myint = 7
print(myint)
```

In the above code, the variable `myint` is assigned the value 7, and then the value is printed to the console.

## Numbers <a name="numbers"></a>

Python supports different types of numbers, including integers and floating-point numbers. Numbers can be used for mathematical calculations.

```python
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
```

The code above demonstrates the use of integers and floating-point numbers in Python. The variable `myfloat` is assigned different values and then printed.

## Strings <a name="strings"></a>

Strings are sequences of characters and can be defined using single quotes ('') or double quotes (""). Strings can be used to store and manipulate textual data.

```python
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes"
print(mystring)
```

In the code above, different strings are assigned to the variable `mystring` and then printed. Strings can contain letters, numbers, symbols, and even special characters like apostrophes.

## Assigning Multiple Variables <a name="assigning-multiple-variables"></a>

Python allows you to assign values to multiple variables in a single line using a technique called multiple assignment.

```python
a, b = 3, 4
print(a, b)
```

In the above code, the values 3 and 4 are assigned to variables `a` and `b` respectively. This is a convenient way to initialize multiple variables simultaneously.

## Arithmetic Operations <a name="arithmetic-operations"></a>

Python supports various arithmetic operations such as addition, subtraction, multiplication, division, and exponentiation.

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

In the code above, arithmetic operations are performed using both numbers and strings. The results are stored in variables and then printed.

## Mixing Operators <a name="mixing-operators"></a>

Mixing operators between different types, such as numbers and strings, is not supported in Python. Attempting to combine incompatible types will result in a TypeError.

```python
# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)
```

The code above demonstrates an example where adding an integer (`one`) with another integer (`two`) and a string (`hello`) raises a TypeError. Operators should be used with operands of compatible types.

## Exercise <a name="exercise"></a>

The code includes an exercise to practice creating variables and performing comparisons. It involves assigning values to variables and checking if they match certain conditions.

The solution to the exercise is provided in the code:

```python
mystring = "Yahallo!"
myfloat = 55.5
myint = 80

if mystring == "Yahallo!":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 55.5:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 80:
    print("Integer: %d

" % myint)
```

The solution assigns specific values to `mystring`, `myfloat`, and `myint` variables and then checks if they satisfy the given conditions. Corresponding messages are printed based on the conditions.

By following this comprehensive documentation, individuals can learn and understand the basics of Python programming, including printing, variables, data types, arithmetic operations, and more. The exercise provides an opportunity to apply the concepts covered in the documentation and strengthen programming skills.
