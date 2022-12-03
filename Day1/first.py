import os

dat = open("input.txt")
t1,t2,t3 = 0,0,0
totals=[]
calories = 0
for line in dat:
    if len(line)>1:
        calories+=int(line)
    else:
        if calories>t1:#cupid shuffl
            t3=t2
            t2=t1
            t1=calories
        elif calories>t2:
            t2=calories            
        elif calories>t3:
            t3=calories
        totals.append(calories)
        calories=0
print(t1+t2+t3)
