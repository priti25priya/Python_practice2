# Write a program to enter all the numbers till the user wants and at the end it should display the sum
# of all the numbers entered.

ch='Y'
sum=0
while ch.upper()== 'Y':
    num=int(input("Enter any number:"))
    sum=sum+num
    ch=input("Do you wish to continue(Y,N):")
print("Sum of all the numbers is:", sum)