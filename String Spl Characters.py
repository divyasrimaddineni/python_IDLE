#String Special Characters:

#1.Concatenation(+): adding 2 strings i.e, 1st string followed by 2nd string.
x="hello world"
#extract "hello" and add "India"
print(x[0:5]+"India")
print(x[0:5]+" "+"India")

#2. Repetition(*):
print("hello"*3)

#(a*b) or (b*a) results the same output.
x="hi"
print(x*3)
print(3*x)

#3.in or not in:

x="python"
print('p' in x)
print('a' not in x)

emps="Ajay,Miller,Blake,rahul,james"
print("John" in emps)
print("james" in emps)
print("blake" in emps) # python is case-sensitive

print("Amar" not in emps)



