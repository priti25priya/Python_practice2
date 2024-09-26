# Constructor: Constructors are generally used for instantiating an object.
# The task of constructors is to initialize(assign values) to the data members of the class
# when an object of the class is created. In Python the __init__() method is called the constructor
# and is always called when an object is created.

class Person():

 def __init__(self):
    print("I am not a robot")
def info(self):
    print(f"{self.name} is a {self.occ}")
a=Person()

# Constructor with arguments:
class Addition:
    first=0
    second=0
    answer=0

    def __init__(self,f,s):
        self.first=f
        self.second=s

    def display(self):
        print("First number:" + str(self.first))
        print("Second number:" + str(self.second))
        print("Addition of the two numbers:" + str(self.answer))

    def calculate(self):
        self.answer=self.first+self.second
# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()

