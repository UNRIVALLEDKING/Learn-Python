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

'''
Here are some basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
%x/%X - Integers in hex representation (lowercase/uppercase)
'''

'''
Exercise
You will need to write a format string which prints out the data using the following syntax: Hello Aditya Kumar. Your current balance is $99.99.
'''

# Solution of the exercise
data = ("Aditya", "Kumar", 99.99)
format_string = "Hello %s %s. Your current balance is $%.2f."
# The %.2f specifier formats the floating-point number with 2 digits after the dot.
print(format_string % data)
