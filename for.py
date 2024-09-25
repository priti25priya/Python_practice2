# For loop: A for loop is used for iterating over a sequence (that is either a list, a tuple,
# a dictionary, a set, or a string).
fruits=["apple","cherry","orange","mango"]
for i in fruits:
    print(i)

# Looping through a string.
for i in "computer":
    print(i)

# The break statement: With the break statement we can stop the loop before it has looped through
# all the items.
animals=["Tiger","Lion","Cow","Leopard","Mouse","Dog"]
for i in animals:
    if i=="Mouse":
     break
    print(i)

# The continue statement: with the continue statement , we can stop the current iteration and continue with
# the next looping iterations.
animals=["Lion","Tiger","Leopard","Cow","Mouse","Dog","Cat","Crocodile"]
for x in animals:
    if x=="Leopard":
        continue
    print(x)

# The range() function: To loop through a set of code a specified number of times, we can use the range()
# function.The range() function returns a sequence of numbers, starting from 0 by default, and increments
# by 1 (by default), and ends at a specified number.
#1.
for x in range(10):
    print(x)

#2.
for i in range (1,11):
    print(i)

# Else in for loop: The else keyword in a for loop specifies a block of code to be executed
# when the loop is finished.
for i in range(0,21):
    print(i)
else:
    print("Finalized")

# Nested loops: It is a loop inside another loop.
#The "inner loop" will be executed one time for each iteration of the "outer loop".
adj=["sweet","sour","tasty"]
noun=["apple","cherry","mango"]

for i in adj:
 for j in noun:
     print(i,j)

# The pass statement: for loops cannot be empty, but if you for some reason have a for loop with no
# content, put in the pass statement to avoid getting an error.
for x in [0,1,3,]:
    pass

# 1.Print the patterns:
print("Number Pattern")

row=5
for i in range(1,row+1,1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")

# 2.Print the patterns:
row=6
for i in range(1,row+1):
    for j in range(i):
        print(i, end=" ")
    print("")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#