#creating a list

x=[10,20,10,30,40,50]# these 5 elements will have different adreesses but not contiguous addresses.

print(x)
print(type(x))
print(id(x))

print(x[0],type(x[0]),id(x[0]))
print(x[1],type(x[1]),id(x[1]))
print(x[2],type(x[2]),id(x[2]))#x[0] and x[2] address are same
