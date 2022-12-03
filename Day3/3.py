

dat = open("./input.txt")
total=0
for line in dat:
    pack1 = line[0:(len(line)//2)]
    pack2 = line[len(line)//2:len(line)]
    print(pack1)
    print(pack2)
    for i in pack1:
        if i in pack2:
            print("Maching char ",i)     
            if ord(i)>90:
                total+=(ord(i)-96)
                print("Value ",(ord(i)-96))
            else:
                total+=((ord(i)-64)+26)
                print("Value ",((ord(i)-64)+26))
            break

print(total)