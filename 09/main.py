# Classes and Objects

# Define a class named MyClass
class MyClass:
    variable = "Yahallo!"  # Object variable

    def function(self):  # Method
        print("This is a message inside the class.")

# Create two objects (instances) of the class MyClass
myobjectx = MyClass()
myobjecty = MyClass()

# Accessing Object Variables
myobjectx.variable  # Access the object variable of myobjectx
myobjecty.variable = "I'm Vengeance"  # Modify the object variable of myobjecty

# Then print out both values
print(myobjectx.variable)  # Output: Yahallo!
print(myobjecty.variable)  # Output: I'm Vengeance

# Accessing Object Functions
myobjectx.function()  # Output: This is a message inside the class.

# init()

# Define a class named NumberHolder with an __init__() method
class NumberHolder:
    def __init__(self, number):
        self.number = number

    def returnNumber(self):
        return self.number

# Create an object var from the class NumberHolder with value 7
var = NumberHolder(7)

# Print the value returned by the returnNumber() method of the object var
print(var.returnNumber())  # Output: 7

'''
Exercise
We have a class defined for vehicles. Create two new vehicles called car1 and car2.
Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.
'''

# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):  # Method to describe the vehicle
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Create two objects car1 and car2 from the class Vehicle
car1 = Vehicle()
car2 = Vehicle()

# Set attributes of car1 to describe a red convertible
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000

# Set attributes of car2 to describe a blue van
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000

# Print the descriptions of car1 and car2 using the description() method
print(car1.description())  # Output: Fer is a red convertible worth $60000.00.
print(car2.description())  # Output: Jump is a blue van worth $10000.00.
