#range(): for generating range of values from 0 to n-1
#ex: x=range(10)------>generates values from o to 9

x=range(10)
print(x)
print(type(x))


#Getting one by one value from the range object using fro loop:

for x in range(10):
    print(x)


y=range(10,20)
for q in y:
    print(q)

#or
    
for q in range(10,20):
    print(q)

z=range(20,30,2) #(startvalue,stopvalue,stepvalue) # incrementing low to high
for s in z:
    print(s)
#or

for s in range(20,30,2):
    print(s)

    
w=range(40,30,-1) # decrementing should be high to low
for t in w:
    print(t)
#or

for t in range(40,30,-1):
    print(t)


z=range(-20,-30,-1) #(startvalue,stopvalue,stepvalue)
for s in z:
    print(s)
#or

for s in range(-20,-30,-1):
    print(s)

w=range(6,10,-1) 
for t in w:
    print(t)#o/p:empty space
