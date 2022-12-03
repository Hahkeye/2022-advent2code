# X = rock   1
# Y = paper   2
# z = scissors   3
# A =rock
# b = paper
# c = scissors

# 0 for loss
# 3 for draw
# 6 for win

WIN = 6
LOSS = 0
DRAW = 3

X = ("X","rock",1)
Y = ("Y","paper",2)
Z = ("Z","scissors",3)
a=X
b=Y
c=Z


dat = open("input.txt")
total = 0
l=-1
for play in dat:
    play = play.split(" ")
    print(play)
    op = play[0]
    you = play[1].strip()
    if op==X[0] and (you==Z[0]): 
        total+=(0+Z[2])
        l=1
    elif op==Y[0] and (you==X[0]):
        total+=(0+X[2])
        l=1
    elif op==Z[0] and (you==Y[0]):
        total+=(0+Y[2])
        l=1
    else:
        if op!=you and l>0:
            match you:
                case "X":
                    total+=(6+X[2])
                case "Y":
                    total+=(6+Y[2])
                case "Z":
                    total+=(6+Z[2])

        else:
            match you:
                case "X":
                    total+=(3+X[2])
                case "Y":
                    total+=(3+Y[2])
                case "Z":
                    total+=(3+Z[2])
    print("Total ",total)
    l=-1

print(total)
    