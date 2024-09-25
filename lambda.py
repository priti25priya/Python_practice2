# Python lambda: A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but have only one expression.
# Syntax= lambda arguments : expression
x=lambda a : a+10
print(x(10))

x=lambda a,b : a*b
print(x(67,89))

# Lambda function: The power of lambda is better shown when we use them as an anonymous function
# inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied
# with an unknown number.
def myfunc(x):
    return lambda a : x*a
mydoubler=myfunc(34)
print(mydoubler(45))
