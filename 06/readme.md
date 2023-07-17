# Chapter 6: Conditions

Welcome to Chapter 6 of the Python Basics Documentation! In this chapter, we will explore conditions in Python. Conditions allow us to check if certain conditions are true or false and execute different blocks of code accordingly. We will cover comparison operators, boolean operators, the `in` operator, the `is` operator, the `not` operator, and more.

## Table of Contents

- [Introduction](#introduction)
- [Comparison Operators](#comparison-operators)
- [Boolean Operators](#boolean-operators)
- [The "in" Operator](#the-in-operator)
- [The "is" Operator](#the-is-operator)
- [The "not" Operator](#the-not-operator)
- [Exercise](#exercise)

## Introduction <a name="introduction"></a>

In this chapter, we will learn about conditions in Python. Conditions allow us to perform different actions based on whether certain conditions are true or false. We will explore various comparison operators, boolean operators, and special operators like `in`, `is`, and `not`. Understanding conditions is crucial for controlling the flow of your program and making decisions based on different scenarios.

## Comparison Operators <a name="comparison-operators"></a>

Comparison operators are used to compare values and evaluate conditions. They return `True` or `False` based on the comparison result. Here are some common comparison operators:

- `==` (equality): Checks if two values are equal.
- `!=` (inequality): Checks if two values are not equal.
- `<` (less than): Checks if the left value is less than the right value.
- `>` (greater than): Checks if the left value is greater than the right value.
- `<=` (less than or equal to): Checks if the left value is less than or equal to the right value.
- `>=` (greater than or equal to): Checks if the left value is greater than or equal to the right value.

## Boolean Operators <a name="boolean-operators"></a>

Boolean operators allow us to combine conditions and perform logical operations. The commonly used boolean operators are:

- `and`: Returns `True` if both conditions are true.
- `or`: Returns `True` if at least one condition is true.
- `not`: Negates the condition. Returns `True` if the condition is false and vice versa.

## The "in" Operator <a name="the-in-operator"></a>

The `in` operator is used to check if a value exists in a sequence, such as a string, list, or tuple. It returns `True` if the value is found and `False` otherwise.

## The "is" Operator <a name="the-is-operator"></a>

The `is` operator is used to compare object identities. It checks if two objects are the same object in memory. It returns `True` if the objects are the same and `False` otherwise.

## The "not" Operator <a name="the-not-operator"></a>

The `not` operator is used to negate a condition. It returns `True` if the condition is false and `False` if the condition is true.

## Exercise <a name="exercise"></a>

In this exercise, you need to change the variables in the provided code to make each if statement resolve as `True`. Currently, some of the conditions are `False`, and you need to modify the variables to make them `True`. This exercise will help you practice using comparison operators, boolean operators, and conditions effectively.

```Python

# change this code
number = 10
second_number = 10
first_array = []
second_array = [1,2,3]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
```

By completing this exercise, you'll gain hands-on experience in manipulating conditions and understanding how different operators affect the outcome.
