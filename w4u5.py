with open("invoice_data.txt", "r") as file:
    line_list = []
    for line in file:
        line.strip()
        item_list = []
        line_split = line.split()
        for element in line_split:
            item_list.append(element)
        line_list.append(tuple(item_list))
        
for line in line_list:
    print(f"{line[0]:15s}{int(line[1]):3d}{float(line[2]):7.2f}{int(line[1])*float(line[2]):8.2f}")