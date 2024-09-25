# Write a program to display the number names of the digits of a number entered by the user.
# For example: if the number is 231, then output should be two three one.

num1=(input("Enter the number:"))
L1=list(num1)
L=len(L1)
i=0
n={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
while (i<L):
    print(n[int(L1[i])], end=" ")
    i=i+1