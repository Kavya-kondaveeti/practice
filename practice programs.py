#maxmimum of two numbers
'''a=10
b=4
print(max(a,b))

#add two numbers
a=10
b=24
c=a+b
print(c)

#factorial of a number

n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial",fact)

# given number is armstrong number or not

n=int(input("Enter a number:"))
x=len(str(n))
temp=n
sum=0
while n>0:
    r=n%10
    sum+=r**x
    n=n//10
if(temp==n):
    print("given number is armstrong number")
else:
    print("not a armstrong number")

#area of a circle

import math
r=5
area=math.pi*(r**2)
print(area)

#check whether a number is prime or not
n=int(input("enter a number:"))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if count==2:
    print("prime num",n)
else:
    print("not a prime num",n)

#check given string is palindrome or not
str=input("enter a string:")
if str==str[::-1]:
    print("string is palindrome")
else:
    print("not a plaindrome")

#ASCII value of a character
a='k'
print(ord(a))'''

#to print fibonacci series

n=int(input("enter a number:"))
print("fibonacci series:")
n1=0
n2=1
count=0
print(n1,end=" ")
print(n2,end=" ")
while count<n:
    res=n1+n2
    print(res,end=" ")
    n1=n2
    n2=res
    count+=1
            


