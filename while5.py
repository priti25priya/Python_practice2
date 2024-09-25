# Print the armstrong number
n=int(input("enter the number:"))
s=n
b=len(str(n))
sum=0
while n!=0:
    r=n%10
    sum=sum+(r**b)
    n=n//10
if s==n:
    print("the given number", s, "is armstrong")
else:
    print("the given number", s, "is not armstrong")