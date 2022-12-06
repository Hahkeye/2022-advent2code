
data = open("input.txt")
pairs = []
c=0
for line in data:
    temp = line.split(",")
    tt = (temp[0].split("-"),temp[1].strip().split("-"))
    tt=([int(tt[0][0]),int(tt[0][1])],[int(tt[1][0]),int(tt[1][1])])

    if (tt[1][0])<=tt[0][0] and tt[1][1]>=tt[0][1]:
        print("---------------------------")
        print("Second contains first")
        print(tt[1][0],"<=",tt[0][0])
        print(tt[1][1],">=",tt[0][1])
        print(tt[0])
        print(tt[1])
        c+=1
        continue
    if (tt[0][0]<=tt[1][0] and tt[0][1]>=tt[1][1]):
        print("---------------------------")
        print("first contains second")
        print(tt[0][0],"<=",tt[1][0])
        print(tt[0][1],">=",tt[1][1])
        print(tt[0])
        print(tt[1])
        c+=1
        continue

print(c)
# for p in pairs:
print(8<=21)
# print(c)


#856
#760
#596
# first contains second
# 21 <= 8
# 71 >= 40
# ['21', '71']
# ['8', '40']



# Second contains first
# 3 <= 8
# 9 >= 44
# ['8', '44']
# ['3', '9']