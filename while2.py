# Write the program to reverse the number from the user.
a=int(input("Enter the number:"))
r=0
rnum=0
while(a!=0):
    r=a%10
    rnum=rnum*10+r
    a=a//10
print("Reversed number is:",rnum)