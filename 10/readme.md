# Dictionaries in Python

Dictionaries are a fundamental data structure in Python that allow you to store and manage key-value pairs. Each element in a dictionary consists of a key and its corresponding value. In this chapter, we'll explore how to create, modify, and access dictionaries, as well as perform common operations with them.

## Creating a Dictionary

In Python, you can create a dictionary using curly braces `{}` and separating each key-value pair with a colon `:`. Here's an example of creating a dictionary:

```python
phonebook = {
    "UNRIVALLEDKING": 938477566,
    "Aditya": 938377264,
    "Luffy": 947662781
}
```

In this example, we have created a dictionary named `phonebook` with three key-value pairs representing the names and corresponding phone numbers.

## Adding and Removing Items

To add a new key-value pair to an existing dictionary, simply assign the value to the new key:

```python
phonebook["NewPerson"] = 123456789
```

This adds a new entry to the `phonebook` dictionary with the key "NewPerson" and the value 123456789.

To remove an item from the dictionary, you can use the `del` keyword or the `pop()` method:

```python
del phonebook["Aditya"]
```

This removes the key "Aditya" and its associated value from the `phonebook` dictionary.

```python
phonebook.pop("Luffy")
```

The `pop()` method removes the item with the specified key ("Luffy" in this case) and returns its value.

## Iterating over a Dictionary

You can iterate over a dictionary using a `for` loop. The loop will iterate over the keys of the dictionary, and you can access the corresponding values using the keys. Here's an example:

```python
for name in phonebook:
    print("Phone number of %s is %d" % (name, phonebook[name]))
```

This loop iterates over the keys in the `phonebook` dictionary and prints the corresponding names and phone numbers.

## Checking for Key Existence

You can check if a key exists in a dictionary using the `in` keyword. For example:

```python
if "UNRIVALLEDKING" in phonebook:
    print("UNRIVALLEDKING is listed in the phonebook.")

if "Luffy" not in phonebook:
    print("Luffy is not listed in the phonebook.")
```

This code checks if "UNRIVALLEDKING" is a key in the `phonebook` dictionary and prints a message accordingly.

## Exercise

Add "UNRIVALLEDKING" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

```Python
phonebook2 = {
 "Aditya" : 938477566,
"UNRIVALLEDKING" : 938377264,
"Luffy" : 947662781
}

# your code goes here

# testing code

if "UNRIVALLEDKING" in phonebook:
 print("UNRIVALLEDKING is listed in the phonebook.")

if "Luffy" not in phonebook:
 print("Luffy is not listed in the phonebook.")

```

## Conclusion

Dictionaries are powerful data structures in Python that allow you to store and retrieve data using keys. They are versatile and widely used for various purposes. By understanding dictionaries and their operations, you can efficiently manage key-value pairs in your Python programs.
