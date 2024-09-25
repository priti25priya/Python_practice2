# Write a program to print the fibonacci series.
n = int(input("Enter the number of terms: "))
a, b = 0, 1
cnt = 0
print("Fibonacci Series:", end=" ")
while cnt < n:
    print(a, end=" ")
    a, b = b, a + b
    cnt += 1


