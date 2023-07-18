## Chapter 9: Classes and Objects 🏎️🧱

In this chapter, we explore the concept of classes and objects in Python. Classes are the building blocks of object-oriented programming, allowing us to create custom data types with their attributes and methods. Objects are instances of classes that represent real-world entities or concepts.

## Classes and Object Variables 📦

In Python, we define a class using the `class` keyword, and within the class, we can define variables, known as object variables, to store data related to objects of that class. Object variables are shared by all instances (objects) of the class.

Let's see an example:

```python
class MyClass:
    variable = "Yahallo!"

    def function(self):
        print("This is a message inside the class.")
```

In this code, we create a class `MyClass` with an object variable `variable` and a method `function`.

## Creating Objects (Instances) 🧱

After defining a class, we can create objects (instances) of that class using the class name followed by parentheses:

```python
myobjectx = MyClass()
myobjecty = MyClass()
```

Here, we create two objects `myobjectx` and `myobjecty` from the class `MyClass`.

## Accessing Object Variables and Functions 🎛️

We can access object variables and functions using the dot notation:

```python
print(myobjectx.variable)  # Output: Yahallo!
myobjectx.function()  # Output: This is a message inside the class.
```

Here, we access the object variable `variable` of `myobjectx` and call the method `function()` on `myobjectx`.

## The `__init__()` Method 🚀

The `__init__()` method is a special method in Python that allows us to initialize object attributes when creating an object. It is called automatically when a new object is created.

Let's see an example:

```python
class NumberHolder:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = NumberHolder(7)
print(var.returnNumber())  # Output: 7
```

In this code, we create a class `NumberHolder` with the `__init__()` method that takes a parameter `number`. When we create an object `var` from this class and pass the value `7`, the `__init__()` method is called, and the `number` attribute is initialized to `7`.

## Exercise 🏋️‍♂️

We have a class defined for vehicles. Create two new vehicles called car1 and car2. Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.

```python
# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

# test code
print(car1.description())
print(car2.description())
```

## Conclusion 🎉

In this chapter, we learned about classes and objects in Python. Classes allow us to create custom data types, and objects represent instances of those classes. We explored how to access object variables and functions and use the `__init__()` method to initialize object attributes. The exercise further solidified our understanding of classes and objects.

Keep practicing and experimenting with classes and objects to master object-oriented programming in Python! 🐍💻
