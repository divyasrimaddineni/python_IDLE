#case4: Defining 2 variables with same name but with different values then
# 2 diff objects gets created and
#the previous object gets removed and moves to the garbage collector.

x=10
x=20
print(x)
print(type(x))
print(id(x))
