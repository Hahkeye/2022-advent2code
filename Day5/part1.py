

stacks = [[],[],[],[],[],[],[],[],[]]

text= None
with open("input.txt") as file:
    text = [next(file) for x in range(8)]
    for line in text:
        for i in range(0,len(line),4):
            if len(line[i-4:i-1].strip()):
                print("Pushing ",line[i-4:i-1]," Onto ",i//4)
                stacks[((i//4)-1)].append(line[i-4:i-1])
            # stacks[(i//3)].append(line[(i-3):i])
    for stack in stacks:
        stack.reverse()
        print(stack)
    # file.readline()
    next(file)
    next(file)
    while True:
        try:
            line = next(file)
        except(StopIteration):
            break
        line = line.split(" ")
        print(line)
        # target=[]
        temp = []
        for i in range(int(line[1])):
            print(i)
            print("Moving to: ",stacks[int(line[5].strip())-1])
            print("From: ",stacks[int(line[3])-1])
            temp.append(stacks[int(line[3])-1].pop())
            # .append()
            # print("Aftrer")
            # print("Moving to: ",stacks[int(line[5].strip())-1])
            # print("From: ",stacks[int(line[3])-1])
        temp.reverse()
        stacks[int(line[5].strip())-1]+=temp
        print("Moving this: ",temp)
        print("After")
        print(stacks[int(line[5].strip())-1])
        temp=[]
        
    file.close()
print(stacks)
for stack in stacks:
    print(stack[len(stack)-1])
# print(len(stacks))

# print(stacks)
# for stack in stacks:
#     stack.reverse()
# stacks.reverse()

