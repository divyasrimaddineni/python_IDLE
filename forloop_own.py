#For loop: we use for loops to repeat some code a certain number of times.
#It allows us to execute a statement or a group of statements multiple times by reducing the burden of writing several lines of code.
#practise problems:
'''
for i in"Divyasri:---":
    print(i)

for i in range(6):
    print(i) #prints from 0 to 5
    

x=['ramya','kavya','divya','navya','divya','sravya']
for names in x:
    print(names)

x=['ramya','kavya','divya','navya','divya','sravya']
for names in x:
    print(names)
    print(x)
    
x=[10,20,30,40,50]
for i in x:
    print(i)
    print("divyasri")


x=['ramya','kavya','divya','navya','divya','sravya']
for names in x:
    print("Cousins")# prints "cousins" 6 times

x=['ramya','kavya','divya','navya','divya','sravya']
for names in x:
    print(names,end=" ")
    print(names,end=" ")
    print(names,end="\n")

#To print "keys" in dictionaries using for loop:
p={'a':'apple','b':'bat','c':'cat'}
for key in p:
    print(key)

#can use keys() to print the keys in dictionaries
p={'a':'apple','b':'bat','c':'cat'}
for v in p.keys():
    print(v)

#To print "values" in dictionaries using for loop:
p={'a':'apple','b':'bat','c':'cat'}
for v in p:
    print(p[v])

#can use values() to print the values in dictionaries:
p={'a':'apple','b':'bat','c':'cat'}
for v in p.values():
    print(v)


#use items() to print both keys and values in dictionaries:
p={'a':'apple','b':'bat','c':'cat'}
for k,v in p.items():
    print(k,v)

p={'a':'apple','b':'bat','c':'cat'}
for v in p.items():
    print(v)
    

#Nested for loop:
l1=[10,20,30,40,50]
l2=[1,2,3,4,5,6]
for i in l1:
    for j in l2:
        print(j,end=" ")
    print(i)

    
#else inside for loop:
x=['apple','ball','cat','dog']
for i in x:
    print(i)
else:
    print("Bye")


#To count no.of elements in a list
x=[1,56,25,48,2,36,5,89,12549,87,33,489,51]
count=0
for i in x:
    count+=1
print(count)


#To find sum of all no's in a list
x=[87,98,568,254]
sum=0
for i in x:
    sum+=i
print(sum)


#To find multiples of 5 in a list and
#count of no's in a list which are divisible by 5

x=[1,5,11,28,30,45,99,65,90,101,10,95,95465]
count=0
for mul in x:
    if mul%5==0:
        print(mul, end=" ")
        count+=1
print("\n",count)

#Using if,elif,else inside for loop:

for i in range(6):
    if i%3==0 and i%5==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizzbuzz")
    else:
        print('---')
'''

#age calculator in 8 to 10 tries, answer should be 'up','down','correct'.
down=0
up=100
for i in range(1,10):
    age=int((down+up)/2)
    result=input("Is your age:"+str(age)+"?") #as input accepts only 1 argument so we are concatenating.
    if result=='correct':
        print('ok!!!')
        break
    elif result=='up':
        down==age
    elif result=='down':
        up==age
    else:
        print("Wrong result!!!")
        


































    
        

































    

