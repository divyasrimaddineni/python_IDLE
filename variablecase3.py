#case3: Defining 2 diff variables with same values then
#only one object gets created& its address is returned to both as same.

x=y=10
print(x,y)
print(type(x), type(y))
print(id(x),id(y))

x=10
y=10.0
print(x,y)
print(type(x), type(y))
print(id(x),id(y))
