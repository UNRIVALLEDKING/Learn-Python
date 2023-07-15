# Basic Operators

# Arithmetic Operators

number = 1 + 2 * 3 / 4.0  # Perform arithmetic operations: addition, multiplication, and division
print(number)

remainder = 11 % 3  # Perform modulus operation (remainder of division)
print(remainder)

squared = 7 ** 2  # Perform exponentiation (7 raised to the power of 2)
cubed = 2 ** 3  # Perform exponentiation (2 raised to the power of 3)
print(squared)
print(cubed)


# Using Operators with Strings

helloworld = "hello" + " " + "world"  # Concatenate strings
print(helloworld)

lotsofhellos = "hello" * 10  # Repeat a string multiple times
print(lotsofhellos)


# Using Operators with Lists

even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers  # Concatenate two lists
print(all_numbers)

print([1, 2, 3] * 3)  # Repeat a list multiple times


'''
Exercise
The target of this exercise is to create two lists called x_list and y_list, which contain 10 instances of the variables x and y, respectively. You are also required to create a list called big_list, which contains the variables x and y, 10 times each, by concatenating the two lists you have created.
'''

x = object()
y = object()

# Solution to the exercise
x_list = [x] * 10  # Create a list with repeated instances of x
y_list = [y] * 10  # Create a list with repeated instances of y
big_list = x_list + y_list  # Concatenate the two lists

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# Testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
