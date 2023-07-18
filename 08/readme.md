# Chapter 8: Functions 🎯

**Table of Contents**

- [What are Functions?](#what-are-functions)
- [Calling Functions in Python](#calling-functions-in-python)
- [Function with Arguments](#function-with-arguments)
- [Function with Return Value](#function-with-return-value)
- [Exercise](#exercise)

## What are Functions? <a name="what-are-functions"></a>

Functions are a fundamental concept in Python that allow you to divide your code into manageable and reusable blocks. By using functions, you can organize your code, make it more readable, and save time by avoiding repetition. Functions also enable you to define interfaces, making it easier for programmers to share and connect their code.

## Calling Functions in Python <a name="calling-functions-in-python"></a>

### Simple Function Example <a name="simple-function-example"></a>

A simple function does not require any arguments and performs a specific task when called.

```python
def my_function():
    print("Hello From My Function!")

# Calling the function
my_function()
```

Output:

```
Hello From My Function!
```

### Function with Arguments <a name="function-with-arguments"></a>

Functions can accept arguments (inputs) to perform tasks based on the given values.

```python
def my_function_with_args(username, greeting):
    print("%s, I'm %s" % (greeting, username))

# Calling the function with arguments
my_function_with_args("UNRIVALLEDKING", "Yahallo!")
```

Output:

```
Yahallo!, I'm UNRIVALLEDKING
```

### Function with Return Value <a name="function-with-return-value"></a>

Functions can also return values using the `return` keyword. The returned value can be used in other parts of the code.

```python
def sum_two_numbers(a, b):
    return a + b

# Calling the function and printing the result
print(sum_two_numbers(2, 5))
```

Output:

```
7
```

## Exercise <a name="exercise"></a>

In this exercise, you'll complete a fully functional program using existing functions and adding your own.

1. Define the `list_benefits()` function that returns a list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together".

2. Define the `build_sentence(info)` function that takes a string argument and returns a sentence starting with the given string and ending with " is a benefit of functions!".

3. Create the `name_the_benefits_of_functions()` function that calls `list_benefits()` to get the list of benefits. Then, iterate through each benefit and print the complete sentence using `build_sentence()`.

```python
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

name_the_benefits_of_functions()
```

By completing this exercise, you'll gain a deeper understanding of functions and how they can work together to create a fully functional program.
