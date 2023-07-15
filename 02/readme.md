# Python Basics - Lists 🚀🔥

This code introduces the concept of lists in Python, which are similar to arrays. Lists can hold variables of any type and any number of variables. They can also be easily iterated over.

## Creating and Modifying Lists

The code begins by creating an empty list called `mylist` using square brackets `[]`. Elements can be added to the list using the `append()` method. In this code, the numbers 1, 2, and 3 are appended to the `mylist`.

```python
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
```

To access elements in the list, square brackets `[]` are used with an index. The index starts from 0, so `mylist[0]` refers to the first element, `mylist[1]` refers to the second element, and so on. The code demonstrates accessing elements in the list using indexing and prints the values.

```python
print(mylist[0])  # prints 1
print(mylist[1])  # prints 2
print(mylist[2])  # prints 3
```

## Iterating over a List

Lists can be easily iterated over using a `for` loop. The loop iterates through each element in the list and executes the specified block of code. In this code, the `for` loop is used to iterate over the elements in `mylist` and print each element.

```python
for x in mylist:
    print(x)
```

## Exception Handling

Attempting to access an index that does not exist in the list will raise an exception (an error). The code demonstrates this by creating a list `[1, 2, 3]` and trying to access `mylist[10]`, which is beyond the bounds of the list.

```python
mylist = [1, 2, 3]
# print(mylist[10])
```

## Exercise

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
