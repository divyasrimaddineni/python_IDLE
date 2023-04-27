#Typecasting: Converting one datatype to other datatype.
#For typecasting--> we have built-in methods such as:
#int(),float(),bool(),str(),list(),tuple(),set(),dict()
'''
#Case1: Converting a string to int
#NOTE: only numerical strings can be converted to integer.
x="10"
print(x,type(x))

y=int(x)
print(y,type(y))
print(x,type(x)) # datatype of x doesn't change.

#Case2: Converting int to string
x=10
print(x,type(x))

y=str(x)
print(y,type(y))

#Case3: Converting float to int
x=4.9
print(x,type(x))

y=int(x)
print(y,type(y)) #decimal part will be ignored.

#converting int to float
s=3987
print(s,type(s))
t=float(s)
print(t,type(t))

#Case4: Converting int to bool
#Any integer can be converted to boolean
#for non-zero value including negative values, bool returns "True"
x=0
print(x,type(x))
y=bool(x)
print(y,type(y)) # o/p:False

x=1
print(x,type(x))
y=bool(x)
print(y,type(y)) #o/p:True

x=8767
print(x,type(x))
y=bool(x)
print(y,type(y))

x=-875
print(x,type(x))
y=bool(x)
print(y,type(y))

x=0.003
print(x,type(x))
y=bool(x)
print(y,type(y))

#Case5: Converting bool to int

x=True
print(x,type(x))
y=int(x)
print(y,type(y))

x=False
print(x,type(x))
y=int(x)
print(y,type(y))

'''
#case6: converting float to 
s=3.14
print(s,type(s))
t=bool(s)
print(t,type(t))
print(s,type(s))





