#Bitwise Operators: Performing operations on bits
#Integers(decimal) are first converted into binary and then
#operations are performed on bit by bit, hence the name bitwise operators.
#Then the result is again returned in decimal format.
'''
1byte=8bits =0000 0000
1KB=1024bytes
1MB=1024KB
1GB=1024MB
'''
#NOTE: Bitwise operators works only on integers.
'''
Various bitwise operators are:

OPERATOR  DESCRIPTION             SYNTAX
&         Bitwise AND               x&y
|         Bitwise OR                x|y
^         Bitwise Exclusive OR      x^y
<<        Bitwise leftshift         x<<y
>>        Bitwise right shift       x>>y
'''

'''
Bitwise operatorse are used for:
N/w sockets or ports
compression and encryption
Graphics
'''

'''
a b a&b  a|b   a^b(i/p should be different)
1 1  1    1     0
1 0  0    1     1
0 1  0    1     1
0 0  0    0     0
'''
#1.Bitwise AND(&): returns 1 if both bits are 1 else returns 0
a=10;b=7
print(a&b)

#2.Bitwise OR(|): returns 1 if any one of the bit is 1 or if both the bits are 1 else return 0
a=10;b=7
print(a|b)

#3.Bitwise XOR(^): Returns 1 if one of the bit is 1 and other is 0 else returns false.
#returns 0 if both the bits are 1 or if both the bits are 0

a=10;b=7
print(a^b)

#4.Bitwise Leftshift(<<): Shift the bits of the number to the left and fills 0 on right i.e.,
#shift the left-most bits i.e, remove bits from left side and add 0's right side.

a=10
print(a<<2) #a<<2: removes 2 bits from left and adds 2 0's at rightside.
print(a<<9) # can add zeroes to the left that too upto the limit
print(a<<98765) # throws error as only 4300 digits for integer conversion and 98765 exceede the limit

#4.Bitwise Rightshift(>>): Shift the bits of the number to the right and fills 0 on left.

a=10
print(a>>2) #a>>2: removes 2 bits from the right and adds 2 0's at leftside.
print(a>>10) # output is zero as we can't add 0's to the right
print(a>>3365) # output is zero






























































