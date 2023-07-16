# Basic String Operations

astring = "Hello world!"  # Define a string using double quotes
astring2 = 'Hello world!'  # Define a string using single quotes

# Print a string containing single quotes
print("single quotes are ' '")

# Print the length of the string
print(len(astring))

# Find the index of the first occurrence of the letter 'o' in the string
print(astring.index("o"))

# Count the number of occurrences of the letter 'l' in the string
print(astring.count("l"))

# Slice the string from index 3 to 7 (exclusive)
print(astring[3:7])

# Slice the string from index 3 to 7 (exclusive) with a step size of 2
print(astring[3:7:2])

# Slice the string from index 3 to 7 (exclusive)
print(astring[3:7])

# Slice the string from index 3 to 7 (exclusive) with a step size of 1
print(astring[3:7:1])

# Reverse the string using slicing
print(astring[::-1])

# Split the string into a list of words using the space delimiter
afewwords = astring.split(" ")
print(afewwords)

'''
Exercise
Try to fix the code to print out the correct information by changing the string.
'''

# Solution of the exercise
s = "Strings are awesome!"

# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])  # Slice the string from start to index 5 (exclusive)
print("The next five characters are '%s'" % s[5:10])  # Slice the string from index 5 to 10 (exclusive)
print("The thirteenth character is '%s'" % s[12])  # Access the character at index 12
print("The characters with odd index are '%s'" % s[1::2])  # Slice the string, starting from index 1, with a step size of 2
print("The last five characters are '%s'" % s[-5:])  # Slice the string from the 5th-from-last character to the end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
