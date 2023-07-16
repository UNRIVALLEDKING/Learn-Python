# Chapter 4: Formatting Strings

Welcome to Chapter 4 of the Python Basics Documentation! In this chapter, we will explore how to format strings in Python using the `%` operator. String formatting allows you to create dynamic strings by substituting variables and values into predefined placeholders.

## Table of Contents

- [Introduction](#introduction)
- [Formatting Strings with `%` Operator](#formatting-strings-with-operator)
- [Argument Specifiers](#argument-specifiers)
- [Exercise](#exercise)

## Introduction <a name="introduction"></a>

In this chapter, we will learn how to format strings in Python using the `%` operator. String formatting enables you to create dynamic strings by replacing placeholders with the values of variables. By understanding string formatting, you can create more readable and customizable output in your programs.

## Formatting Strings with `%` Operator <a name="formatting-strings-with-operator"></a>

The `%` operator is used for string formatting in Python. It allows you to substitute variables and values into a string by specifying placeholders and providing the values in a tuple. Here are some examples:

```python
# This prints out "Hello, UNRIVALLEDKING!"
name = "UNRIVALLEDKING"
print("Hello, %s!" % name)

# This prints out "UNRIVALLEDKING is 19 years old."
name = "UNRIVALLEDKING"
age = 19
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1, 2, 3]
print("A list: %s" % mylist)
```

In the code above, the `%s` and `%d` are placeholders for string and integer values, respectively. The values are provided in a tuple after the `%` operator. The `%` operator replaces the placeholders with the corresponding values, resulting in formatted strings.

## Argument Specifiers <a name="argument-specifiers"></a>

When using the `%` operator for string formatting, you can use different argument specifiers to control the formatting of values. Here are some commonly used argument specifiers:

- `%s` - String (or any object with a string representation, like numbers)
- `%d` - Integers
- `%f` - Floating-point numbers
- `%.<number of digits>f` - Floating-point numbers with a fixed number of digits after the dot
- `%x/%X` - Integers in hex representation (lowercase/uppercase)

You can use these argument specifiers to customize the formatting of values within the string.

## Exercise <a name="exercise"></a>

Now, let's practice formatting strings! In this exercise, your task is to write a format string that prints out the data using the following syntax: "Hello Aditya Kumar. Your current balance is $99.99." Here's the exercise code:

```python
data = ("Aditya", "Kumar", 99.99)
format_string = "Hello %s %s. Your current balance is $%.2f."

print(format_string % data)
```

In the code above, the `%s` specifier is used for strings, the `%f` specifier is used for floating-point numbers, and `%.2f` specifies that the floating-point number should have two digits after the dot.

By completing this exercise, you'll gain hands-on experience in formatting strings and applying argument specifiers to create customized output.
