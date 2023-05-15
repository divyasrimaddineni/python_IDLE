#List slicing: Extracting particular elements of a list

x=[10,20,30,40,50,60]
#extract 1st 3 elements--->10,20,30:
print(x[0:3])#always upperbound is excluded
print(x[:3])
print(x[-6:-3])

#extract---->30,40,50
print(x[2:5])
print(x[5:2]) #empty list b/c always slicing is in forward direction
print(x[-4:-1])

#Extract--->30 to 60
print(x[2:6])
print(x[2: ])
print(x[-4: ])

print(x[:])
print(x)
print(x[0:])

print(x[0:6:2])
print(x[::2])

print(x[::-1]) #reverse the elements


