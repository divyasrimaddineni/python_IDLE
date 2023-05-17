x=[[10,20,30],['div',78.98,-34.87],[56,0.01,0]]

print(x,len(x))
#printing each sub-lists.

print(x[0],type(x[0]),len(x[0]))
print(x[1],type(x[1]),len(x[1]))
print(x[2],type(x[2]),len(x[2]))

print("\n") #'\n'--->two line gap

#printing each sub-list uding for loop
for p in x:
    print(p,type(p),len(p))

#printing each element of each sub-list using nested for loop:

for p in x:
    for q in p:
        print(q,type(q))
#In the above example, for every value of p,inner for loop executes for 3 times.

        
