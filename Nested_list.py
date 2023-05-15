#Nested list: lists within a list

x=[['Kohli',55],['Rohith',35],['Hardik',60],['Dhoni',40]]

print(x,len(x))

for p in x:
    print(p,type(p))

print("\n")


for p,q in x:
    print("PLAYER:",p)
    print("RUNS:",q)
    print("================")

#Compute the total score of all the players:
score=0
for p,q in x:
    score=score+q
print("TOTAL SCORE:",score)
