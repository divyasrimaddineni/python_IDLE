#complex datatype: For creating complex numbers.
#ex: x+yj
#complex numbers are comprised of 2 parts:
#1.real part(keyword:real) --->float type.
#2.imaginary part(keyword:imag) --->float type.
#we use "cmath" file to import complex number operations.

x=3+4j
print(x)
print(type(x))
print(x.real)
print(x.imag)

#A complex number can also be created by using complex function.
x=complex(3,-5)
print(x)

y=complex(0.2,0.5)
print(y)

z=complex(3,) # or z=complex(3)
print(z)

s=complex()
print(s) #o/p:0j
print(s.real) #o/p:0.0
print(s.imag) #o/p:0.0

s=complex(1293)
print(s) #o/p: (1293+0j)

w=complex("5-7j")
print(w)

#using "cmath"

import cmath
z=1325.46+764.756j
print("the real part is:",(z.real))
print("the imaginary part is:",z.imag)


import cmath
x=2353;y=83.327
z=complex(x,y)
print("the real part is:",end=" ") #"end" is used to print the next print value in this line after ':'
print(z.real)
print("the imaginary part is:",end=" ")
print(z.imag)



