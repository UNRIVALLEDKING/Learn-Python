# Lists

# Create an empty list
mylist = []

# Append elements to the list
mylist.append(1)  # Add the number 1 to the list
mylist.append(2)  # Add the number 2 to the list
mylist.append(3)  # Add the number 3 to the list

# Access elements in the list using indexing
print(mylist[0])  # Print the first element of the list (1)
print(mylist[1])  # Print the second element of the list (2)
print(mylist[2])  # Print the third element of the list (3)

# Iterate over the elements of the list
for x in mylist:
    print(x)  # Print each element in the list (1, 2, 3)

# Accessing an index that does not exist generates an exception (an error).
mylist = [1, 2, 3]
# print(mylist[10])  # This line of code will raise an IndexError since index 10 is out of range

'''
Exercise
In this exercise, you need to add numbers and strings to the correct lists using the "append" list method. Add the numbers 1, 2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the "strings" list.

Additionally, assign the second name in the "names" list to the variable "second_name" using the brackets operator []. Remember that indexing starts from 0, so the second item has an index of 1.
'''

# Create empty lists for numbers and strings
numbers = []  # Initialize an empty list to store numbers
strings = []  # Initialize an empty list to store strings

# List of names
names = ["John", "Eric", "Jessica"]  # Create a list of names

# Solution of the exercise
numbers.append(1)  # Add the number 1 to the "numbers" list
numbers.append(2)  # Add the number 2 to the "numbers" list
numbers.append(3)  # Add the number 3 to the "numbers" list

strings.append("hello")  # Add the string 'hello' to the "strings" list
strings.append("world")  # Add the string 'world' to the "strings" list

second_name = names[1]  # Access the second name in the list (Eric)

# Print the filled arrays and the second name in the names list
print(numbers)  # Print the contents of the "numbers" list
print(strings)  # Print the contents of the "strings" list
print("The second name on the names list is %s" % second_name)  # Print the second name (Eric) from the "names" list
