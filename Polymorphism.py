# Polymorphism: he word polymorphism means having many forms. In programming, polymorphism
# means the same function name (but different signatures) being used for different types.
class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

# Method overloading: Two or more methods have the same name but different numbers of
# parameters or different types of parameters, or both. These methods are called overloaded
# methods and this is called method overloading.
#
# Like other languages (for example, method overloading in C++) do, python
# does not support method overloading by default. But there are different ways to
# achieve method overloading in Python.
# code
def add(a=None, b=None):
    # Checks if both parameters are available
    # if statement will be executed if only one parameter is available
    if a != None and b == None:
        print(a)
    # else will be executed if both are available and returns addition of two
    else:
        print(a+b)


# two arguments are passed, returns addition of two
add(2, 3)
# only one argument is passed, returns a
add(2)

# Method overriding: Method overriding is an ability of any object-oriented programming language that
# allows a subclass or child class to provide a specific implementation of a method that is already
# provided by one of its super-classes or parent classes.

# 1.super().__init__(): This ensures that the parent class’s constructor is called,
# initializing any attributes defined in the parent class. It’s good practice to call the parent
# class constructor if it does important initialization.
# 2.Method Override: The Child class overrides the show() method of the Parent class,
# so when show() is called on an instance of Child, it uses the Child class’s implementation.

# Python program to demonstrate
# Defining parent class
class Parent():

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"

    # Parent's show method
    def show(self):
        print(self.value)

    # Defining child class


class Child(Parent):

    # Constructor
    def __init__(self):
        super().__init__()  # Call parent constructor
        self.value = "Inside Child"

    # Child's show method
    def show(self):
        print(self.value)

    # Driver's code


obj1 = Parent()
obj2 = Child()

obj1.show()  # Should print "Inside Parent"
obj2.show()  # Should print "Inside Child"

#
#