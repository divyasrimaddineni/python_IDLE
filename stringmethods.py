#string methods: Methods are used only for Strings but not for list,tuple,... .
#NOTE: All string methods returns new values, they donot change the original string.
#Remember python is "case-sensitive".


#1.upper(): to print in uppercase
x="hyderabad"
print(x.upper())

abc="DelHi"
print(abc.upper())


#2.lower(): to print in lowercase
x="MUMBAI"
print(x.lower())

#NOTE: "casefold()" is similar to "lower()" but it's bit more aggressive.
#For example, the German letter ß is already lowercase so, the lower() method doesn't make the conversion.
#But the casefold() method will convert ß to its equivalent character 'ss'.


#3.capitalize(): capitaizing the 1st character of a string
x="india is my country"
print(x.capitalize()) #o/p: India is my country

x="india Is My Country"
print(x.capitalize()) #o/p: India is my country

x="India Is My Country"
print(x.capitalize()) #o/p: India is my country

#4.title(): for capitalizing the 1st char of each word in a string
x="good evening hyderabad"
print(x.title())

#reatime usage:
emps="rahul,ajay,divya,blake,miller,amar"
print(emps.title())

#5.swapcase: for converting one case to another case
x="Good evEning hyderabad"
print(x.swapcase())

#6.replace(): for replacing a portion of the string
x="java is easy and JAVA is simple"
print(x.replace("java","python"))

y="Sachin is a good batsman"
print(y.replace("Sachin","Kohli"))

x="India is my country"
print(x.replace("India is my country","I am an Indian"))
print(x) # string methods will not change/affect the original string.
print(x.replace("ia",'ian'))
print(x.replace("ia",'ian'),x.replace("try","tries"))
print(x.replace("ia",'ian '),"\n",x.replace("try","tries"))

#7.count(): To count the no.of occurences of a particular character or a substring.
x="hello hello hello...how are you???"
print(x.count("hello"))
print(x.count("h"))

x="hello hello hello...how are you???, HELLO!!, are you OK??, Man!!!...."
print(x.count("."))
print(x.count(".."))
print(x.count("!"))
print(x.count("ar"))
print(x.count("ae"))
print(x.count(","), x.count("hello"),x.count("ll"))

data='''1.python is simple
2. python Is user-friendly
3.python supports interactive mode
4.python supports 89300 modules
5.python has many built-in libraries
6.python supports object-oriented programming
7.python supports all major databases
8.python is dynamic typed
9.python provides simple syntaxes
10.python is extensible.
'''
print(data.count('python'))
print(data.count('is')) #As python is case-sensitive,it produces output as '3' instead of '4' b/c in "Is", "I" is capital. 

#8.format(): for substitutions
x="{} is the captain of Indian team"
print(x.format("Rohith"))

y="his name is {} and he is a {}"
print(y.format("Rahul","doctor"))

z="{} is the {} of {}"
print(z.format('Delhi','Capital','India'))
print(z.format("Modi","PM","India"))
print(z.format("Rohit","Captain",'India'))

w="{} {} and {} are the trending technologies"
print(w.format("Python",'AWS','Devops'))

print("Myself {0} and I am a {1}".format("Divya","Girl"))
print("Myself {name} and I'm {age}".format(name="Divya",age="23"))

w="{0} {1} and {2} are the trending technologies"
print(w.format("Python",'AWS','Devops'),"\n",w.format("C","java","C++"))

w="{2} {0} and {1} are the trending technologies"
print(w.format("Python",'AWS','Devops'))


#9. strip(): To remove blansapces before and after the string
#rstrip():to remove space at rightside of string.
#lstrip():to remove space at left side of string
x="        Good evening Hyd         "
print(x,len(x))
y=x.strip()
print(y)
print(len(y))

z="        Good evening Hyd         "
print(z,len(z))
print(z.strip())
print(z,len(z)) # strip method won't modify the 'z' value and it's length.

x="    good     mrng    divyasri     "
print(x)
print(len(x))
xyz=x.strip()
print(xyz)
print(len(xyz))

#10.find(): To check whether a sub-string is available or not
#If the sub-string is found it returns the 1st character index position else
# it returns '-1'.
x="python is easier than java"
print(x.find('java')) # it returns 'j' position in 'java'
print(x.find('python'))
print(x.find('y'))
print(x.find('hadoop')) # returns '-1'
print(x.find('zy')) # returns -1


#11. split(): If we split a string, we get a list
#to split, we can specify a seperator, or the default seperator is whitespace.

x='good evening papa'
print(x.split()) #o/p:['good', 'evening', 'papa']

x='Good evening Hyderabad'
y=x.split(" ") # splitting based on spaces
print(y,type(y)) # o/p:['Good', 'evening', 'Hyderabad'] <class 'list'>
print(y[2]) # prints Hyderabad from list 2nd position


emp="101,Ajay,700000,manager"
y=emp.split(",")
print(y)
# to print name and designation
print(y[1],y[3])

y="hi,how are you?, how's ur life?"
print(y.split(",")) #['hi', 'how are you?', " how's ur life?"]

z="hii#how r u? are you ok? !"
print(z.split("#"), z.split("?")) #['hii', 'how r u? are you ok? !'] ['hii#how r u', ' are you ok', ' !']

#12.startswith(),
#endswith()

x="python is easier than java"
print(x.startswith("python")) # returns True
print(x.endswith('java'))

x='divya is a brave girl'
print(x.startswith('is')) #returns False
print(x.endswith('girl')) #returns True


#13.join(): To join the strings of a collection

date=["18","04","2023"]
y="/".join(date)
print(y)

y='-'.join(date)
print(y)

#In dictionaries,when using an iterable, the returned values are keys but not values.
x={"name":"divya","age":"23","sex":"female"}
y="AND".join(x)
print(y) #o/p:nameANDageANDsex

x=("divya","sri","Maddineni")
y="+".join(x)
print(y)

#14.isalpha(): It returns'True' if all the characters within the string are alphabets.
x="virat kohli" # there is a space in between so it's False.
print(x.isalpha())

city='hyderabad'
print(city.isalpha())

city='hydera123bad  xyz654'
print(city.isalpha())

#15.isdecimal(): It returns 'True' if all the characters within the strings are numeric.
pi='3.14'
print(pi.isdecimal()) # there is a dot in between, so it's False.

date="19 04 2023"
print(date.isdecimal()) # there is space in between, so it's False

accno="30963465637"
print(accno.isdecimal())

#accno=30963465637 print(accno.isdecimal())# it shows error as 'int' object has no attribute 'isdecimal'

#16.isalnum(): It returns 'True' if all the characters within the string are either alphabets or numericals or combination of both.

accno="30963465637"
print(accno.isalnum())

city='hyderabad'
print(city.isalnum())

pan="ALG86347379"
print(pan.isalnum())

#17.index(): same as find() but the only difference is if the substring is not found then it produces 'valueError'.
s="Hello"
print(s.index("Hello"))

print(s.index("hello")) #produce value error.

#To deal with value errors we use exception handling.
s="Hello divyasri"
try:
    print(s.index("Sravyasri"))
except ValueError:
    print("Substring is not found")
    































