#String: A string is a sequence collection of characters.
#In python, a string represented using:
#1.single quote(' ')
#2.double quote(" ")
#3.Triple quote('''  ''')

'''
Each character of a string is represented or accessed by a unique index.
String supports 2 types of indexes:
    1. Positive index or forward index---->index starts from left to right -->starts with 0
    2. negative index or backward index---->index starts from right to left -->starts with -1
'''

x="python"
print(x)
print(type(x))
print(len(x))

print(x[3])
print(x[-3])

y="programming"
print(x+y) #concatenation: adding 2 strings i.e., 1st string followed by 2nd string
print(x " "+y)
