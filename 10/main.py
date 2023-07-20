# Dictionaries

# Create an empty dictionary named phonebook
phonebook = {}

# Add key-value pairs to the phonebook
phonebook["UNRIVALLEDKING"] = 938477566
phonebook["Aditya"] = 938377264
phonebook["Luffy"] = 947662781

# Print the phonebook dictionary
print(phonebook)

# Alternatively, create a dictionary named new_phonebook using dictionary literal syntax
new_phonebook = {
    "UNRIVALLEDKING": 938477566,
    "Aditya": 938377264,
    "Luffy": 947662781
}

# Print the new_phonebook dictionary
print("new_phonebook", new_phonebook)

# Iterating over dictionaries using a for loop
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Removing a value from the phonebook using the 'del' keyword
del phonebook["Aditya"]
print("phonebook", phonebook)

# Removing a value from the new_phonebook using the 'pop' method
new_phonebook.pop("Luffy")
print("new_phonebook", new_phonebook)

'''
Exercise
Add "UNRIVALLEDKING" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.

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
'''

# Solution to the Exercise

# Define the phonebook2 dictionary with the given key-value pairs
phonebook2 = {  
    "Aditya": 938477566,
    "UNRIVALLEDKING": 938377264,
    "Luffy": 947662781
}

# Add "UNRIVALLEDKING" with the phone number 938273443 to the phonebook2
phonebook2["UNRIVALLEDKING"] = 938273443

# Remove "Luffy" from the phonebook2 using the 'pop' method
phonebook2.pop("Luffy")

# Test whether "UNRIVALLEDKING" and "Luffy" are in the phonebook2 and print the results
if "UNRIVALLEDKING" in phonebook2:
    print("UNRIVALLEDKING is listed in the phonebook.")
    
if "Luffy" not in phonebook2:
    print("Luffy is not listed in the phonebook.")
