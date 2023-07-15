# Basic Operators

This code provides an introduction to basic operators in Python. It covers arithmetic operations, string concatenation and repetition, and list concatenation. The code also includes an exercise to practice creating and manipulating lists.

## Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations in Python. The code demonstrates various arithmetic operations:

```python
number = 1 + 2 * 3 / 4.0
remainder = 11 % 3
squared = 7 ** 2
cubed = 2 ** 3
```

The `number` variable stores the result of the arithmetic expression `1 + 2 * 3 / 4.0`, which evaluates to `2.5`. The `remainder` variable stores the remainder of the division `11 % 3`, which is `2`. The `squared` variable stores the square of `7`, which is `49`. The `cubed` variable stores the cube of `2`, which is `8`.

## Using Operators with Strings

Python allows the use of operators with strings to perform concatenation and repetition. The code demonstrates these operations:

```python
helloworld = "hello" + " " + "world"
lotsofhellos = "hello" * 10
```

The `helloworld` variable concatenates the strings "hello", a space, and "world" using the `+` operator, resulting in the string "hello world". The `lotsofhellos` variable repeats the string "hello" ten times using the `*` operator, resulting in the string "hellohellohellohellohellohellohellohellohellohello".

## Using Operators with Lists

Operators can also be used with lists in Python. The code showcases list concatenation and repetition:

```python
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1, 2, 3] * 3)
```

The `all_numbers` list is created by concatenating the `odd_numbers` list and the `even_numbers` list using the `+` operator. The resulting list contains the numbers [1, 3, 5, 7, 2, 4, 6, 8]. The last line demonstrates repetition, where the list [1, 2, 3] is repeated three times using the `*` operator, resulting in the list [1, 2, 3, 1, 2, 3, 1, 2, 3].

## Exercise

The target of this exercise is to create two lists called `x_list` and `y_list`, which contain 10 instances of the variables `x` and `y`, respectively. You are also required to create a list called `big_list`, which contains the variables `x` and `y`, 10 times each, by concatenating the two lists you have created.

```python
x = object()
y = object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []


# After executing the solution, `x_list` contains 10 instances of object `x`, `y_list` contains 10 instances of object `y`, and `big_list` contains the concatenation of `x_list` and `y_list`.

## Testing Code

# The code includes testing conditions to verify the correctness of the exercise solution:


if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
```

These conditions check if `x_list` contains exactly 10 instances of object `x` and if `big_list` contains exactly 10 instances of both object `x` and object `y`. If the conditions are satisfied, corresponding messages are printed.

This code serves as a comprehensive introduction to basic operators in Python and demonstrates their usage in arithmetic operations, string manipulation, and list manipulation. The exercise provides an opportunity to practice and apply the concepts covered in the code.
