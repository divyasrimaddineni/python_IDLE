#1.Arithmetic operators: For performing arithmetic operations.
#various arithmetic operators are:
'''
1.Addition(+)
2.Subtraction(-)
3.multiplication(*)
4.Division(/) --> returns quotient with decimals
5.floor division(//) --> returns quotient without decimals
6.Modulo division(%) --> returns remainder
7.Exponent(**)
'''

x=10;y=4

add=x+y
print("Sum =",add)

sub=x-y
print("Sub =",sub)

mul=x*y
print("Product =",mul)

div=x/y
print("Division =",div)

floordiv=x//y
print("floordivision =",floordiv)

moddiv=x%y
print("Modulodivision =",moddiv)

exp=x**y
print("exponent =",exp)

x=10;y=3;print(x**y)

print(10/3)
print(10//3)
print(10%3)

#Arithmetic operations on int and float
print(10+3.3)
print(10-3.3)
print(10*3.3)
print(10/3.3)
print(10//3.3)
print(10%3.3)

#Arithmetic operations on float and boolean
#True=1, False=0
print(4.5+True)
print(4.5-True)
print(4.5*True)
print(4.5/True)
print(4.5//True)
print(4.5%True)

print(4.5+False)
print(4.5+False)

#Arithmetic operations on boolean and boolean
print(True+True)
print(True-True)
print(True*True)
print(True/True)
print(True//True)
print(True%True)

print(False+False)
print(False-False)
print(False*False)
print(False/False)
print(False//False)
print(False%False)

#Arithmetic operations on int and string
#print("hello"+3)
print("hello"+"3") #o/p:hello3
print("hello"+str(3)) #o/p:hello3
print("hello"*str(3))
print("hello"*3)
print(3*"hello")
































