# Map: The map () function returns a map object(which is an iterator) of the results after
# applying the given function to each item of a given iterable (list, tuple, etc.).

def cube(x):
    return x*x*x

print(cube(2))

l=[1,2,4,3,6,3]

newl=list(map(cube, l))
print(newl)

# Filter: The filter() method filters the given sequence with the help of a function
# that tests each element in the sequence to be true or not.

def filter_function(a):
    return a>4

newnewl=list(filter(filter_function, l))
print(newnewl)
