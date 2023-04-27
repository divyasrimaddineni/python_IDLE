#3.Logical Operators: These operators gives logical relationship b/w 2 objects.
#logical operators also returns True or False.

#various logical operators are:
'''
1.and
2.or
3.not

x y xandy  xory 
T T  T       T
T F  F       T
F T  F       T
F F  F       F
'''
x=10;y=20;z=30
p=(x>y) and (z>x)
print(p)

q=(x>y) and (y>x) or (z!=y)
print(q)

r=(x>y) and (z==x+y) or (y==z-x)
print(r)

print(not True)
print(not False)







