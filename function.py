# Python functions: A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# 1.To print geometric mean:
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
a=9
b=8

calculateGmean(a,b)

c=7
d=5
calculateGmean(c,d)

# 2. To print geometric mean with if statement:
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
a=9
b=7
if a>b:
    print("First number is greater")
else:
    print("Second number is greater or equal")
calculateGmean(a,b)

c=10
d=90
if c>d:
    print("First number is greater")
else:
    print("Second number is greater")
calculateGmean(c,d)

# 3. To print geometric mean and greater number using functions.

def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater")
a=34
b=23

calculateGmean(a,b)
isGreater(a,b)

c=56
d=89

calculateGmean(c,d)
isGreater(c,d)

# Function arguments:
def average(a=9,b=1):
    print("The average is", (a+b)/2)
average(b=9)

def name(fname, mname="John",lname="singh"):
    print("Hello", fname,mname,lname)
name("Amy","Sammuel","Watson")


# Function using dictionary:
def name(**name):
    print("Hello,", name["fname"],name["mname"],name["lname"])

name(fname="James",mname="Barnes",lname="Warner")

# Return a value:
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)

c=average(7,8,4,9,10)
print(c)
