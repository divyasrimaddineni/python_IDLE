#List addresses

x=[10,20,30,40,50]
y=[10,20,30,40,50]

print(x,id(x))
print(y,id(y))

print(x is y) # False as the addresses are not same.

#NOTE: 2 mutable objects with same elements always returns 2 different objects with 2 different addresses.
    # 2 immutable objects with same content returns only one object with one address.

print(x[0],type(x[0]),id(x[0]))    
print(y[0],type(y[0]),id(y[0]))
#address is same for both x[0] and y[0] as values are same i.e.,'10'.

z=[10,20,30,40,50]
w=[1,2,3]
z=w #'z' takes 'w' values
    #w=z i.e., 'w' takes 'z' values
print(z[0],type(z[0]),id(z[0]))    
print(w[0],type(w[0]),id(w[0]))
print(z is w)


