# If else statement
num=200
if num>199:
    print("number is positive")
else:
    print("number is non-positive")

# Elif: The elif keyword is Python's way of saying "if the previous conditions were not true,
# then try this condition".
a=89
b=89
if a>b:
    print("The value of a is greater than b")
elif a==b:
    print("a and b are true")

# Else: The else keyword catches anything which isn't caught by the preceding conditions.
a=700
b=76
if b>a:
    print("The value of b is greater than the value of a")
elif a==b:
    print("Both the values are equal")
else:
    print("The value of a is greater than the value of b")

# Write a program to check whether a person is eligible of voting or not
age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible for voting")
else:
    print("Sorry! you are not eligible for voting")

# Write a program to find the lowest number out of the two numbers accepted by the user.
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
if num1>num2:
    print("The smallest number is:", num2)
else:
    print("The smallest number is:",num1)


