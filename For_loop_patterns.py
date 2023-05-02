#For loop patterns:

#1.Floyd's triangle:

'''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
#solution:
for i in range(1,10): # for no.of rows
    for j in range(1,i+1):#range(1,i)-->range(1,1) i.e, 1 executes '0' times
        #or for j in range(0,i)
        print(i,end="")
    print()

#2:
'''
1
12
123
1234
12345
123456
1234567
12345678
123456789
'''
#solution:
for i in range(1,10):
    for j in range(1,i+1):
        print(j,end="")
    print()

#3.
'''
*
**
***
****
*****
******
*******
********
*********
'''
#solution:
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end="")
    print()

#4.
'''
A  
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
HHHHHHHH
IIIIIIIII
'''
#ASCII values for:
'''
A-65
B-66
.
.
Z-90

a-97
b-98
..
z-122
'''
#solution:
for i in range(1,10):
    for j in range(1,i+1):
        print(chr(i+64),end="")
    print()

#5.
'''
A
AB
ABC
ABCD
ABCDE
ABCDEF
ABCDEFG
ABCDEFGH
ABCDEFGHI
'''
#solution:
for i in range(1,10):
    for j in range(1,i+1):
        print(chr(j+64),end="")
    print()

#6.Pascal Triangle:
'''
              *
             * *
            * * *
           * * * *
          * * * * *
         * * * * * *
        * * * * * * *
       * * * * * * * *
      * * * * * * * * *
'''
#solution:
n=20 # for 20 blank spaces
for i in range(1,10):
    print(' '*n,end="")
    print('* '*i,end="")
    print()
    n-=1 # or n=n-1

#7.
'''
1
22
333
4444
55555
666666
7777777
666666
55555
4444
333
22
1
'''
#solution:
for i in range(1,8):
    for j in range(1,i+1):
        print(i,end="")
    print()
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()
#8.
'''
1
12
123
1234
12345
123456
1234567
123456
12345
1234
123
12
1
'''
#solution:
for i in range(1,8):
    for j in range(1,i+1):
        print(j,end="")
    print()
for i in range(6,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

#9.
'''
999999999
88888888
7777777
666666
55555
4444
333
22
1
'''
#solution:
for i in range(9,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()

#10.
'''
123456789
12345678
1234567
123456
12345
1234
123
12
1
'''

#11.
'''
987654321
98765432
9876543
987654
98765
9876
987
98
9
'''

#12.
'''
AAAAAAAAA
BBBBBBBB
CCCCCCC
DDDDDD
EEEEE
FFFF
GGG
HH
I
'''

#13.
'''
ABCDEFGHI
ABCDEFG
ABCDEF
ABCDE
ABCD
ABC
AB
A
'''

#14.
'''
55555
 4444
  333
   22
    1
    '''

#15.
'''
12345
 1234
  123
   12
    1
    '''

#16.
'''
ABCDE
 ABCD
  ABC
   AB
    A
    '''

#17.
'''
ABCDE
 ABCD
  ABC
   AB
    A
    '''

#18.
'''
555555555 -9TIMES
 4444444  -7TIMES
  33333   -5TIMES
   222    -3TIMES
    1     -1TIME
'''

#19.
'''
999999999
 7777777
  55555
   333
    1
'''

#20.
'''
123456789
 1234567
  12345
   123
    1
'''

































