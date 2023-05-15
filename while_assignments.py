#while loop assignments:

#1.pgm to reverse a given number:
 #input: n=123, the reversed number is 321

#solution:
n=int(input("enter value of n:"))
print("the reversed number is:",end='')
while(n>0):
    rem=n%10
    print(rem,end='')
    n=n//10
'''
Tracing:

n=123
123>0 True
rem=123%10=>3
print->3
n=123//10=>12
-----------------------
n=12
12>0 True
rem=12%10=>2
print->2
n=12//10=>1
-------------------------
n=1
1>0 True
rem=1%10=>1
print->1
n=1//10=>0
-------------------------
n=0
0>0 False
while condition failed
'''

#2.pgm to compute the digitalsum of a number
 #input:n=123, the digital sum is-->1+2+3=6
  #(sum of the digits of a given of a number)

#solution:
sum=0
n=int(input("enter value of n:"))
while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
print("Digital sum=",sum)

#3.pgm to check whether a given number is a palindrome or not
 #palindrome:If we reverse, we need to get the same number
#solution:
n=int(input("enter value of n:"))
temp=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if (rev==temp):
    print(temp,"is a palindrome")
else:
    print(temp,"is not a palindrome")
'''
Tracing:
n=121
temp=121
rev=0
121>0 True
rem=121%10 =1
rev=0*10+1 =1
n=121//10 =12
----------------------
n=12
temp=121
rev=1
12>0 True
rem=12%10 =2
rev=1*10+2 =12
n=12//10 =1
-----------------------
n=1
temp=121
rev=12
1>0 True
rem=1%10 =1
rev=12*10+1 =121
n=1//10 =0
---------------------------
n=0
temp=121
rev=121
0>0 False
comes out of while loop

rev==temp
121==121------->palindrome
'''


#4.Pgm to check whether a given number is Armstrong number
 #n=153 is armstrong number:
  #if the sum of the cubes of the digits of the number is equal to the
  #same number then it is a armstrong number.

#solution:
sum=0
n=int(input("enter value of n:"))
temp=n
while(n>0):
    rem=n%10
    sum=sum+rem*rem*rem
    n=n//10
if(sum==temp):
    print(temp,"is armstrong number")
else:
    print(temp,"is not a armstrong number")

#5.pgm to find the factorial of a number
#solution:
temp=1
n=int(input("enter the value:"))
while(n>1):
    temp=temp*n
    n=n-1
print("the factorial of ",n,"is:",temp)


#6.pgm to check whether a given number is a strong number or not.
'''
  n=145 is a strong number
   1!+4!+5!
   =1+24+120
   =145 which is aequal to the same number
'''
#solution:
sum=0
n=int(input("enter the value:"))
temp=n
while(n>0):
    num=1
    rem=n%10
    
    while(rem>=1):
        num=num*rem
        rem=rem-1
    sum=sum+num
    n=n//10

if(sum==temp):
    print(temp, "is a strong number")
else:
    print(temp,"is not a strong number")

#7.pgm to check whether a given number is unique number or not.
'''n=1089 is a unique number
 ex:take any number ---------------->1089
    multiply with highest digit----->  *9
                                     ------
                                      9801---->reverse it--->we need to get
                                      same number-->its unique num
                                      '''
#8.pgm to check whether a given number is a perfect number or not
'''n=6 is a perfect number
  factors of 6 is--->1+2+3=6
  If the sum of the factors is equal to the given number then it is a perfect number.
  '''
#solution:
n=int(input("enter the value:"))
sum=0
i=1
while(n>i):
    if(n%i==0):
        sum=sum+i
    i=i+1
if(sum==n):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
    

#9.pgm to check whether a given number is prime no or not
#solution:
    
n=int(input("enter the value:"))
count=0
i=2
while(i<=n//2):
    if(n%2==0):
        count=count+1
        break
    i=i+1
if(count==0 and n!=1):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")



#10.pgm to check whether a given number is even or odd.
#solution:
    
n=int(input("enter the value:"))
while(n):
    if(n%2==0):
        print(n,"is even number")
    else:
        print(n,"is odd number")
    break
  
