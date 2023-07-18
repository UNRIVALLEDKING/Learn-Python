# Functions

'''
What are Functions?
Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.'''

def my_function():
    print("Hello From My Function!")
    

def my_function_with_args(username, greeting):
    print("%s I'm %s"%(greeting,username))



def sum_two_numbers(a, b):
    return a + b

# How do you call functions in Python?

my_function()

my_function_with_args("UNRIVALLEDKING", "Yahallo!")
print(sum_two_numbers(2,5))



'''
Exercise
In this exercise you'll use an existing function, and while adding your own to create a fully functional program.

Add a function named list_benefits() that returns the following list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

Add a function named build_sentence(info) which receives a single argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

Run and see all the functions work together!


# Modify this function to return a list of strings as defined above
def list_benefits():
    return []

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return ""

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()'''

# Solution to the exercise

# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return ("%s is a benefit of functions!"%benefit)

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()