# 1. Try and except statement: Try and except statements are used to catch and handle exceptions
# in Python.

a=input("Enter the number:")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i}={int(a)*i}")
except:
    print("Invalid output")
print("End of program")

# 2. Try with else clause: In Python, you can also use the else clause on the try-except block
# which must be present after all the except clauses.
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

# 3. Finally keyword: Python provides a keyword finally, which is always executed after the
# try and except blocks. The final block always executes after the normal termination of the
# try block or after the try block terminates due to some exception.
try:
    k = 5//0
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print('This is always executed')

