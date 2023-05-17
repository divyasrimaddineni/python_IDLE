#Different ways of creating a list:2 ways

#1. using []
#2. using list() --->list() accepts only one argument and
         #that argument should be iterable type like string,list,tuple,set.

#creating a list using list()
x=list()  #empty list is created
print(x)
print(type(x))
print(len(x))

#ex:2 Creating a list from a string.
x=list("python")  #empty list is created
print(x)
print(type(x))
print(len(x))

#ex:3
'''
x=list("python","Java") #Error-->list() accepts only one argument.
print(x)
print(type(x))
print(len(x))
'''

#ex:4
'''
x=list(10)  #error b/c 'int' is not iterable
print(type(x))
print(len(x))
'''
#ex:5
x=list([10,20,30,40,50])  
print(x)
print(type(x))
print(len(x))

#ex:6
x=list((10,20,30,40,50)) #tuple converted to list i.e., typecasting 
print(x)
print(type(x))
print(len(x))
