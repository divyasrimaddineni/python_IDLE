#break stmt: When break stmt is used within a loop then ctrl comes out of that loop
#            and stmts after break are not executed.
#break works with "for loop" as well.


#ex:
x=1
while(True):
    print("Hello")
    if(x==5):
        break
        print("hi..")#stmts after break are not executed
    x=x+1

print("end")
