# While loop: With the while loop we can execute a set of statements as long as a condition is true.
i=0
while i<10:
    print(i)
    i+=1

# First 10 even numbers
num=2
while num<=20:
    print(num)
    num=num+2

# First 10 odd numbers
num=1
while num<=20:
    print(num)
    num=num+2

# Write a program to print first 10 integers and their squares using while loop:
num=1
print("Numbers\t\tSquares")
while num<=10:
    print(num,"\t\t\t",num**2)
    num=num+1

# Write a program to print the following series: 10,20,30....300
num=10
while num<=300:
    print(num,end=",")
    num=num+10

# Write a program to print the following series: 105,98,91....7:
num=105
while num>=7:
    print(num, end=",")
    num=num-7

# Write a program to print first 10 natural numbers in reverse order:
num=10
while num>=0:
    print(num)
    num=num-1

# Write a program to print all the even numbers that falls between two numbers (both are included) entered from
#the user using while loop.
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
if num1>num2:
    while (num1>num2):
      if num2%2==0:
          print(num2)
      num2=num2+1
else:
    while(num2>num1):
        if num1%2==0:
            print(num1)
        num1=num1+1

# Write a program to check whether a number is prime or not using while loop:
num1 = int(input("Enter any number: "))
k = 0
if num1 == 0 or num1 == 1:
    print("Not a prime number")
else:
    i = 2
    while i < num1:
        if num1 % i == 0:
            k = k + 1
        i += 1
    if k == 0:
        print(num1, "is a prime number")
    else:
        print(num1, "is not a prime number")

# Write a program to find the sum of the digits from the user.
num=int(input("Enter the number:" ))
r=0
sum=0
while(num!=0):
    r=num%10
    sum=sum+r
    num=num//10
print("The sum of the digits are:" , sum)

# Write a program to find the product of digits from the user.
x=int(input("Enter the number:"))
r=0
p=1
while(x!=0):
    r=x%10
    p=p*r
    x=x//10
print("The product of the digits are:",p)

