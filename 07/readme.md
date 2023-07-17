# Loops

Loops are used in programming to execute a block of code repeatedly. They allow you to iterate over a sequence of elements or perform a task until a certain condition is met. In this chapter, we'll explore different types of loops in Python: the `for` loop and the `while` loop.

## The "for" Loop

The `for` loop is used to iterate over a sequence (such as a list, tuple, or string) or any other iterable object. It executes a block of code for each element in the sequence. Here's an example:

```python
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
```

This code prints out each prime number in the `primes` list.

You can also use the `range()` function to generate a sequence of numbers and iterate over it using a `for` loop. Here are some examples:

```python
# Prints out the numbers 0, 1, 2, 3, 4
for x in range(5):
    print(x)

# Prints out 3, 4, 5
for x in range(3, 6):
    print(x)

# Prints out 3, 5, 7
for x in range(3, 8, 2):
    print(x)
```

## The "while" Loop

The `while` loop is used to repeatedly execute a block of code as long as a given condition is true. It keeps iterating until the condition becomes false. Here's an example:

```python
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count by 1 in each iteration
```

This code prints out the numbers 0, 1, 2, 3, 4 by using a `while` loop.

## "break" and "continue" Statements

Inside loops, you can use the `break` statement to exit the loop prematurely and the `continue` statement to skip the current iteration and proceed to the next one.

Here's an example that demonstrates the use of `break` and `continue`:

```python
# Prints out the numbers 0, 1, 2, 3, 4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1, 3, 5, 7, 9
for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
```

## "else" Clause for Loops

In Python, loops can have an optional `else` clause that is executed when the loop is completed, but not if the loop is terminated by a `break` statement. This is useful when you want to perform certain actions after the loop has finished executing normally.

Here are examples of using the `else` clause with loops:

```python
# Prints out 0, 1, 2, 3, 4, and then prints "count value reached 5"
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" % count)

# Prints out 1, 2, 3, 4
for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
else:
    print("This is not printed because the for loop is terminated by a break statement.")
```

## Exercise

In the exercise, you need to loop through and print out all the even numbers from the `numbers` list in the same order they are received. However, you should stop printing numbers once you encounter the number 237 in the sequence.

```python
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers:
```

By following this code documentation, you can learn how to use loops effectively in Python to iterate over sequences and perform repetitive tasks.
