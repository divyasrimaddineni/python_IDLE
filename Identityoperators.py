#Identity Operators: used to compare the addresses of 2 objects
#Identity operators also returns True or False.
#Identity operators are:
#1.is
#2.is not

#ex1:
x=10;y=20

print(x,id(x))
print(y,id(y))

print(x is y) #compares the addresses
print(x==y) #compares the content(comparision operators)
print(x is not y)

#ex2:
a=10;b=10
print(a,id(a))
print(b,id(b))
print(a is b)
print(a == b)
print(a is not b)

