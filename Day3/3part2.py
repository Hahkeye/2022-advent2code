

dat = open("./input.txt")
total=0
lines=[]
for line in dat:
    lines.append(line)

for i in range(0,len(lines),3):
    elf1 = lines[i]
    elf2 = lines[i+1]
    elf3 = lines[i+2]
    for i in elf1:
        if i in elf2 and i in elf3:
            print("Maching char ",i)     
            if ord(i)>90:
                total+=(ord(i)-96)
                print("Value ",(ord(i)-96))
            else:
                total+=((ord(i)-64)+26)
                print("Value ",((ord(i)-64)+26))
            break

    # print(elf1)
    # print(elf2)
    # print(elf3)
    # for i in pack1:
    #     if i in pack2:
    #         print("Maching char ",i)     
    #         if ord(i)>90:
    #             total+=(ord(i)-96)
    #             print("Value ",(ord(i)-96))
    #         else:
    #             total+=((ord(i)-64)+26)
    #             print("Value ",((ord(i)-64)+26))
    #         break

print(total)