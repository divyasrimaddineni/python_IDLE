#print(): output function or output statement in python

x=10
y=20
print(x,y)

print(x,",",y) # we can't concatenate integers
print(x,y,sep=",")
print(x,y,sep=" ")
print(x,y,sep="\t")
print()
print(x,y,sep="\n")
print(x,y,sep=":");print(x,y,sep="-->")


a,b,c=10,20,30
print(a,b,c)

a=10;b=20;c=30
print(a);print(b);print(c)
print(a,b,c,sep=' ')

#NOTE: a=10,b=20,c=30 gives error

print("good",end=" ") # "end" used to attach the next print statement to the following print statement
print("Evening")

print("good",end="\t")
print("Evening")


print("good",end="\n")
print("Evening")

print("good",end=" ")
print("Evening",end=" ")
print("hyderabad")



