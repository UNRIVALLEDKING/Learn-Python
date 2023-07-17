# Conditions

# Comparison Operators
x = 2
print(x == 2)  # Prints out True: checks if x is equal to 2
print(x == 3)  # Prints out False: checks if x is equal to 3
print(x < 3)  # Prints out True: checks if x is less than 3

# Boolean Operators
name = "UNRIVALLEDKING"
age = 19
if name == "UNRIVALLEDKING" and age == 19:
    print("Your name is UNRIVALLEDKING, and you are also 19 years old.")

if name == "UNRIVALLEDKING" or name == "Aditya":
    print("Your name is either UNRIVALLEDKING or Aditya.")

# The "in" Operator
name = "UNRIVALLEDKING"
if name in ["UNRIVALLEDKING", "Aditya"]:
    print("Your name is either UNRIVALLEDKING or Aditya.")

# Conditional Statements
statement = False
another_statement = True
if statement is True:
    # do something if the statement is True
    pass
elif another_statement is True:  # else if
    # do something else if another_statement is True
    pass
else:
    # do another thing if both conditions are False
    pass

# if-else Statements
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

# The 'is' Operator
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True: checks if the values of x and y are equal
print(x is y)  # Prints out False: checks if x and y are the same object in memory

# The "not" Operator
print(not False)  # Prints out True: negates the value of False (True)
print((not False) == (False))  # Prints out False: checks if the negated value of False is equal to False

'''
Exercise

Change the variables in the first section, so that each if statement resolves as True.

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
'''

# Solution to the Exercise
number = 20
second_number = False
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")  # Resolves as True: number is greater than 15

if first_array:
    print("2")  # Resolves as True: first_array is not empty

if len(second_array) == 2:
    print("3")  # Resolves as True: length of second_array is 2

if len(first_array) + len(second_array) == 5:
    print("4")  # Resolves as True: sum of lengths is 5

if first_array and first_array[0] == 1:
    print("5")  # Resolves as True: first_array is not empty and its first element is 1

if not second_number:
    print("6")  # Resolves as True: second_number is False
