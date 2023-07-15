# Lists
'''
Lists are similar to arrays. They can hold variables of any type and any number of variables. Lists can be easily iterated over. Here's an example of how to build a list.
'''

# Create an empty list
mylist = []

# Append elements to the list
mylist.append(1)
mylist.append(2)
mylist.append(3)

# Access elements in the list using indexing
print(mylist[0])  # prints 1
print(mylist[1])  # prints 2
print(mylist[2])  # prints 3

# Iterate over the elements of the list
for x in mylist:
    print(x)

# Accessing an index that does not exist generates an exception (an error).
mylist = [1, 2, 3]
# print(mylist[10])

'''

Exercise
In this exercise, you need to add numbers and strings to the correct lists using the "append" list method. Add the numbers 1, 2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the "strings" list.

Additionally, assign the second name in the "names" list to the variable "second_name" using the brackets operator []. Remember that indexing starts from 0, so the second item has an index of 1.
'''

# Create empty lists for numbers and strings
numbers = []
strings = []

# List of names
names = ["John", "Eric", "Jessica"]

# Solution to the exercise
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]  # Access the second name in the list

# Print the filled arrays and the second name in the names list
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)