# Chapter 3: Basic Operators

Welcome to Chapter 3 of the Python Basics Documentation! In this chapter, we will explore basic operators in Python. Operators are symbols that perform operations on variables and values. Understanding and utilizing operators is crucial for performing computations and manipulating data in Python.

## Table of Contents

- [Introduction](#introduction)
- [Arithmetic Operators](#arithmetic-operators)
- [Using Operators with Strings](#using-operators-with-strings)
- [Using Operators with Lists](#using-operators-with-lists)
- [Exercise](#exercise)
- [Further References](#further-references)

## Introduction <a name="introduction"></a>

In this chapter, we will cover various basic operators in Python that enable you to perform arithmetic calculations, concatenate strings, and manipulate lists. Operators allow you to perform different operations on variables and values, providing a powerful toolset for your programming tasks.

## Arithmetic Operators <a name="arithmetic-operators"></a>

Arithmetic operators are used to perform mathematical calculations in Python. Here are some commonly used arithmetic operators:

```python
number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
```

The above code demonstrates the use of arithmetic operators such as addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), modulus (`%`), and exponentiation (`**`). These operators allow you to perform calculations and obtain results based on mathematical operations.

## Using Operators with Strings <a name="using-operators-with-strings"></a>

In Python, operators can also be used with strings. Here are examples of using operators with strings:

```python
helloworld = "hello" + " " + "world"
print(helloworld)

lotsofhellos = "hello" * 10
print(lotsofhellos)
```

The code above demonstrates the concatenation operator (`+`) to join strings together and the repetition operator (`*`) to repeat a string multiple times. These operators provide flexibility in working with strings, allowing you to combine and manipulate them as needed.

## Using Operators with Lists <a name="using-operators-with-lists"></a>

Operators can be used with lists to perform operations like concatenation and repetition. Here's an example:

```python
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1, 2, 3] * 3)
```

The code above demonstrates the concatenation operator (`+`) to combine two lists into a single list and the repetition operator (`*`) to repeat a list multiple times. These operators provide convenient ways to manipulate and combine lists effectively.

## Exercise <a name="exercise"></a>

Now, let's practice using operators! In this exercise, your goal is to create two lists called `x_list` and `y_list`, which contain 10 instances of the variables `x` and `y`, respectively. You are also required to create a list called `big_list`, which contains the variables `x` and `y`, 10 times each, by concatenating the two lists you have created. Here's the exercise:

```python
x = object()
y = object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# Testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
```

The solution to the exercise is provided in the code. It demonstrates how to use the repetition operator (`*`) to create lists with repeated elements and the concatenation operator (`+`) to combine lists.

## Further References <a name="further-references"></a>

If you'd like to explore more about Python's operators and their usage, refer to the following resources:

- [Python Documentation on Operators](https://docs.python.org/3/library/operator.html)
- [Real Python - Python Operators: Arithmetic, Logical, Comparison, Bitwise & More](https://realpython.com/python-operators/)
- [W3Schools Python Tutorial - Python Operators](https://www.w3schools.com/python/python_operators.asp)

By referring to these resources, you can expand your knowledge and dive deeper into the world of operators in Python.

By following this documentation and completing the exercise, you'll gain a better understanding of basic operators in Python and their application in various scenarios.

Happy coding with basic operators!
