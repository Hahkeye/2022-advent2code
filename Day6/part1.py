


chars = []
data = open("input.txt")
count = 0
track =0
max=0
# print(data)
for i in data:
    for x in i:
        print("i ",x)
        x=x.strip()
        if len(chars)<14:
            chars.insert(0,x)
            count+=1
            print("IChars: ",chars)
        else:
            chars.pop()
            chars.insert(0,x)
            count+=1
            print("EChars: ",chars)
            # print("cout1: ",chars.count(chars[0]))
            # print("cout2: ",chars.count(chars[1]))
            # print("cout3: ",chars.count(chars[2]))
            # print("cout3: ",chars.count(chars[3]))
            for char in chars:
                if chars.count(char)==1:
                    print(track)
                    track+=1
                if track==14:
                    print("THE NUM<BE: ",count)
                    max=count
                    break
            if track==14:
                break
            # if track>max:
            #     max=track
            track=0
print("max ",max)
            # if chars.count(chars[0]) == 1 and chars.count(chars[1]) == 1 and chars.count(chars[2]) == 1 and chars.count(chars[3]) == 1:
            #     print(count)
            #     break