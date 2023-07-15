# Python Basics - Lists 🚀🔥

**Table of Contents**

- [Introduction](#introduction)
- [Lists and Modifying Lists](#lists-and-modifying-lists)
- [Accessing Elements in a List](#accessing-elements-in-a-list)
- [Iterating over a List](#iterating-over-a-list)
- [Exception Handling](#exception-handling)
- [Exercise](#exercise)

## Introduction <a name="introduction"></a>

This code provides an introduction to the concept of lists in Python. Lists are versatile data structures that can hold variables of any type and any number of elements. This code demonstrates how to create and manipulate lists, access elements by indexing, iterate over the list, and handle exceptions. It also includes an exercise to practice adding elements to lists and accessing elements by index.

## Lists and Modifying Lists <a name="lists-and-modifying-lists"></a>

The code begins by creating an empty list called `mylist` using square brackets `[]`. Elements can be added to the list using the `append()` method. In this code, the numbers 1, 2, and 3 are appended to `mylist`.

```python
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
```

## Accessing Elements in a List <a name="accessing-elements-in-a-list"></a>

To access elements in the list, square brackets `[]` are used with an index. Indexing starts from 0, so `mylist[0]` refers to the first element, `mylist[1]` refers to the second element, and so on. The code demonstrates accessing elements in the list using indexing and prints the values.

```python
print(mylist[0])  # prints 1
print(mylist[1])  # prints 2
print(mylist[2])  # prints 3
```

## Iterating over a List <a name="iterating-over-a-list"></a>

Lists can be easily iterated over using a `for` loop. The loop iterates through each element in the list and executes the specified block of code. In this code, the `for` loop is used to iterate over the elements in `mylist` and print each element.

```python
for x in mylist:
    print(x)
```

## Exception Handling <a name="exception-handling"></a>

Attempting to access an index that does not exist in the list raises an exception (an error). The code demonstrates this by creating a list `[1, 2, 3]` and trying to access `mylist[10]`, which is beyond the bounds of the list. The line is commented out to prevent the exception.

```python
mylist = [1, 2, 3]
# print(mylist[10])
```

## Exercise <a name="exercise"></a>

The code presents an exercise where you need to add numbers and strings to the appropriate lists. The `numbers` list should contain the numbers 1, 2, and 3 using the `append()` method. The `strings` list should contain the words 'hello' and 'world'. Additionally, the variable `second_name` is assigned the second name in the `names` list using indexing (`names[1]`).

```python
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None

second_name = names[1]  # Access the second name in the list

# Print the filled arrays and the second name in the names list
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
```

By following this code documentation, you can understand the basics of lists in Python and practice adding elements to lists and accessing them by index.
