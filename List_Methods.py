#List Methods:

#1.append(): for appending the element at the end of the list
            #it accepts only one argument at a time.
x=[10,20,30,40,50]
print(x,len(x))
x.append(60)
print(x,len(x))
#x.append(70,80)#append() accepts only one argument at a time.
x.append([15,25,35])#[15,25,35] is one argument of type list.
print(x,len(x))

#using for loop and append(),appending multiple elements:
for p in (55,65,75): #or for p in [55,65,75]:
    x.append(p)
print(x,len(x))

#2.extend():For extending a list with the elements of other list.
y=[1.5,2.5,3.5,4.5,5.5] #list elements will add but not list.
x.extend(y)
print(x,len(x))

#3.insert(index,value)): inserting an element at the desired position.
x.insert(2,25)
x.insert(4,'mumbai')
print(x,len(x))

#4.pop(index): removing an element based on index.
x.pop(5)
print(x,len(x))

#remove the element '55' using pop()
#Firstly find the index of '55' and then pop it
#we use index() to find the index of an element.

#5.index(element): returns the index of an element.
print(x.index(55))
x.pop(8)
print(x)

#6.remove(element): removes an element based on value.
x.remove(30)
x.remove('mumbai')
#print(x.remove('mumbai')) # its not possible, it displays 'None'
print(x,len(x))

#ex:
emps=[[101,'Miller',50000,'hyd'],
      [102,'blake',60000,'pune'],
      [103,'James',70000,'chennai']]
#Task: remove "city" field from every list.
#i)using pop():
'''
for p in emps:
    p.pop(3)
print(emps)
'''
#ii)using remove():

for p in emps:
    p.remove(p[3])
print(emps)


#ex:
emps=[[101,'Miller',50000,'hyd'],
      [102,'Blake',60000,'pune'],
      [103,'James',70000,'chennai']]

#Task: Extract only empnames and sort them in order
names=[]
for p in emps:
    names.append(p[1])
print(names)
print(sorted(names)) # sorting based on ASCII values.

#7.sort():
z=[30,10,50,40,20]
z.sort()
print(z)
#print(z.sort()) # displays 'None'

#8.count():counts the no.of occurences of an element in a list.
medals=['IND','AUS','ENG','IND','JAP','AUS','IND','JAP']
print(medals.count('IND')) # it doesn't create a list as output but it gives number as output

#9.reverse():
a=[1,2,3,4,5,6]
a.reverse()
print(a)

#10.copy():duplicating a list
b=a.copy() # we are not assigning addresses
print(b)

print(a,id(a))
print(b,id(b))

c=b # we are explicitly assigning the addresses
print(c,id(c))
print(b,id(b))





    






































        








    

