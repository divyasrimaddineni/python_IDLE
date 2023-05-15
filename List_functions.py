#List Functions:
x=[20,10,50,40,30]

print(x)
print(type(x))
print(len(x))
print(sum(x))
print(max(x))
print(min(x))
print(sorted(x))#as we sorted also insertion order of x doesn't change
print(sorted(x,reverse=True))
print(x[::-1])
print(sorted(x[::-1]))#first it reverse then it sorts
print(sorted(x[::-1],reverse=True))

print(reversed(x)) #it reverses the elements and stores the result in
        #another object and displays that object address

#Apply for loop to get one by one element from the reversed object
for p in reversed(x):
    print(p,end=' ')
print("\n")

for p in reversed(sorted(x)):# first it sorts then it reverse
    print(p)



y=[20,10,50,40,30,10.25]

print(y)
print(type(y))
print(len(y))
print(sum(y))
print(max(y))
print(min(y))
