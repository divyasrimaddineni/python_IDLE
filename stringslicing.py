#String Slicing: Extracting particular portion of a string
# x[m:n]---> 'm' is the starting and 'n' is ending that gives 'n-1' as output
#positive indexing: starts with zero(0,1,2,3,.....)
#Negative indexing: starts with -1(-1,-2,-3,.....)

x="python program"
print(x)

#extract "python"
print(x[0:6])

#extract "prog"
print(x[7:11])
print(x[11:7]) #output as empty string b/c always slicing in forward direction.

#extract "prog" using negative indexing
#negative indexing if done in reverse direction, output is blank.
print(x[-7:-3]) #negative indexing should done in forward direction.

#extract "program"
print(x[7:14])
print(x[7:])
print(x[7: ])

print(x[-7: ])

print(x[ :6])
print(x[:6])

print(x[:])
print(x[ : ])
print(x)
print(x[0: ])
print(x[0:])

print(x[-7:11])

#Slicing with step values:

print(x[0:14:2])#startvalue,stopvalue,stepvalue
print(x[0:14:])

'''
NOTE:
1.print(x[a:b:-c]) --> Stepvalue can be negative but it doesn't throw any error but output is not generated if a<b
but
case1:print(x[::-c]) is allowed and it's used to reverse the string and it produces output in reverse manner.
case2:print(x[a::-c])
case3:print(x[:b:-c])
case2 and case3 works.
2.print(x[a:b:0]) and print(x[::0]) --> Stepvalue can't be zero as it throws error.
'''

print(x[::2]) #print(x[: : 2]) is also same as print(x[::2])
print(x[::-1]) #reverse the elements of a string

print(x[14::-1]) #reverse the elements of a string

print(x[:5:-1])
print(x[:-9:-1])

#palindrome: If we reverse a string, we need to get the same string then it is a palindrome.
#ex: madam,malayalam,dad

x="madam"
print(x)
print(id(x))
y=x[::-1]
print(y)
print(id(y))

#Ex:
s='offer letter'
print(s[0:1:3])
print(s[-1:-2:-3])

#Ex:
s='python program'

print(s[-1:-6:-1])
print(s[-1:-6:-2])

print(s[-6:-1])

print(s[-6:-1:-2])#o/p: blank space

print(s[:-1])# or print(s[0:-1])

print(s[-6:-1:2])

print(s[-6:-1:-2])

print(s[-6:-1:2])

print(s[-1:-2:-3])

