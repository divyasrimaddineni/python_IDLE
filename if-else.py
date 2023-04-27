#Syntax for defining "if-else":
'''
if(condition):
    stmt1}
    stmt2}----> Block1
    stmt3}
    stmt4}
else:
    stmt5}
    stmt6}--->Block2
    stmt7}
    stmt8}

If the condition is True, then the stmts within the if-block(Block1) will be executed.
If the condition is False, then the stmts within the else-block(Block2) will be executed.
'''

#Pgm illustrating if-else:

x=int(input("Enter value of x:"))
y=20
print(y)

if(x<=4):
    print("ONE")
    print("TWO")
    print("THREE")
    print("FOUR")
else:
    print("FIVE")
    print("SIX")
    print("SEVEN")
    print("EIGHT")

#NOTE: Either 1or4or2orany spaces considered as indentation if all the stmts are followed the same space then it won't give any error.

x=int(input("Enter value of x:"))

if(x<=4):
 print("ONE")
 print("TWO")
 print("THREE")
 print("FOUR")
else:
    print("FIVE")
    print("SIX")
    print("SEVEN")
    print("EIGHT")
