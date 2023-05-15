#continue: It skips the current iteration and continues with the next iterations.

x=0
while(x<10):
    x=x+1
    if(x==5):# when x=5, it skips this entire iteration.
        continue
        print("hi") 
    print(x,"hello")
print("end")

#ex:
x=0
while(x<=5):
    print("hi")
    if(x==3):
        continue
        print("hello")
    print(x,"number")
    x=x+1
print("end")

