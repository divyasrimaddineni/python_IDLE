#Accepting marks of 5 subjects and compute the total and percentage
#and also the class or grade awarded

s1=90;s2=80;s3=70;s4=60;s5=50

total=s1+s2+s3+s4+s5

per=(total/500)*100

print("TOTAL=",total)

print("PERCENTAGE=",per)

if(per>=70):
    print("FIRST CLASS WITH DISTINCTION!!!")
elif(per>=60):
    print("FIRST CLASS!!!")
elif(per>=50):
    print("SECOND CLASS!!!")
elif(per>=40):
    print("THIRD CLASS!!!")
else:
    print("FAIL!!!")
