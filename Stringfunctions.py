#String Functions:

x="hello"

#1.len(): Returns the no.of characters within a string
print(len(x))

#2.max(): returns the max valued character
print(max(x))

#3.min(): returns the min valued character
print(min(x))

#NOTE: min() and max() are based on ASCII values.
'''
Space(null)-32
!-33
"-34
#-35
.
.
.

A-65
B-66
C-67
.
.
.
Z-90

a-97
b-98
c-99
.
.
.
'''

y="Hello"
print(min(y))

z="Virat Kohli"
print(min(z)) # min of z is "space"

w="python3"
print(min(w))



