# Reduce: The reduce function is used to apply a particular function passed in its
# argument to all of the list elements mentioned in the sequence passed along.
# This function is defined in “functools” module.

from functools import reduce

numbers=[1,2,3,4,5]

def mysum(x,y):
    return x+y

sum=reduce(mysum, numbers)

print(sum)