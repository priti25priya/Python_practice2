# Classes: A class is a user-defined blueprint or prototype from which objects are created.
# Creating a new class creates a new type of object, allowing new instances of that type to be made.
class Person():
    name="Hammy"
    occupation="Software developer"
    Networth=1000

a=Person()
a.name="Priti"
a.occupation="Data engineer intern"
print(a.name, a.occupation)

# Self parameter:
class Person():
    name="Hammy"
    occupation="Software developer"
    Networth=1000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()
b=Person()
a.name="Priti"
a.occupation="Data engineer intern"

b.name="John"
b.occupation="Accountant"
a.info()
b.info()


#
#
#
#
#
#
#
#