lines = []
with open("numbers.txt", "r") as file:
    for line in file:
        lines.append(int(line.strip()))
        #line1 = line.strip()
        #line2 = int(line1)
        #lines.append(line2)

lines.sort(reverse=True)
for i in lines[:3]:
    print(i)

#lines.sort()
#for i in lines[:-4:-1]:
#    print(i)

#for i in range(3):
#    maximum = max(lines)
#    print(maximum)
#    lines.remove(maximum)
