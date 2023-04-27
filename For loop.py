#For loop: for loop executes set of stmts for every element of collection object.
#All the stmts within the for loop should follow the indentation.

x=[10,20,30,40,50]
y=x[::-1]
print(y)
for p in x:
    print(p)
for q in y:
    print(q)

#printing all the values within a single line

for p in x:
    print(p,end=" ")

#reverse printing the elements

for p in x[::-1]:
    print("\n",p)

