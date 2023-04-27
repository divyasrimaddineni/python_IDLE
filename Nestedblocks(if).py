#Nested blocks: Blocks within a block
'''
if(condition):
    stmt1
    stmt2
    stmt3
    if(condition):#inner if
        stmt5
        stmt6              
    else: #inner else
        stmt7
        stmt8
    stmt9}
    stmt10}-->outer if stmts
    stmt11}
else:
    stmt12
    stmt13
    stmt14
'''

#pgm to find the largest of 3 no's:
x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
z=int(input("Enter the value of z:"))

if(x>y):
    if(x>z):
        print(x,"is the largest number")
    else:
        print(z,"is the largest number")
else:
    if(y>z):
        print(y,"is the largest number")
    else:
        print(z,"is the largest number")

       #or       
'''
if(x>y)&(x>z):
    print(x,"is the largest number")
elif(y>x)&(y>z):
    print(y,"is the largest number")
else:
    print(z,"is the largest number")
'''

    
