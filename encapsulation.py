#Encapsulation : It refers to the concept of bundling the data (attributes) and methods (functions) into a single unit called a class.
# Encapsulation in python: In Python, encapsulation is achieved through the use of access modifiers.
#The three common access modifiers are:

# Public: Members are accessible from outside the class.
# Protected: Members are accessible within the class and its subclasses.
# Private: Members are only accessible within the class.

# 1. Public:(Public members in class):
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Alice", 20)
print(student.name)  # Accessing public attribute

# 2. Protected: (Protected members in class):
class Animal:
    def __init__(self):
        self._type = "Unknown"

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self._type = "Dog"

dog = Dog()
print(dog._type)

# 3. Private:(Private members in class):
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())  # Accessing private method