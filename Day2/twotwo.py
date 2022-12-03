dat = open("input.txt")
# rock = a
# paper =b
# sci = c
val2 = {"X":0,"Y":3,"Z":6}
val = {"X":1,"Y":2,"Z":3}
def check(first,second):
    convert = {"X":"A","Y":"B","Z":"C"}
    second = convert[second]
    if first == second:
        return 3
    elif (first == "A" and second == "C") or (first =="B" and second=="A") or (first =="C" and second=="B"):
        return 0
    else:
        return 6


def lose(first,second):
    if second == "X":
        for i in val.keys():
            if check(first,i)==0:
                return (check(first,i)+val[i])
    elif second == "Y":
        for i in val.keys():
            if check(first,i)==3:
                return (check(first,i)+val[i])
    elif second == "Z":
        for i in val.keys():
            if check(first,i)==6:
                return (check(first,i)+val[i])
total=0
# for play in dat:
#     play = play.split(" ")
#     op = play[0]
#     you = play[1].strip()
#     result = check(op,you)
#     your = val[you]
#     print("------------------------")
#     print("Result from ",result)
#     print("You get ",your)
#     print(result+your)
#     total+=(result+your)

for play in dat:
    play = play.split(" ")
    op = play[0]
    you = play[1].strip()
    result = lose(op,you)
    total+=(result)
print(total)
