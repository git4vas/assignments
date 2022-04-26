table = []
rows = int(input("Please enter the number of rows in the matrix: "))
columns = int(input("Please enter the number of columns in the matrix: "))
print("Enter the matrix values:")
for r in range(1, rows + 1):
    items = []
    for c in range(1, columns + 1):
        list_item = int(input("Value: "))
        items.append(list_item)
        #print ("items = ", items)
    table.append(items)
    #print("table = ", table)

for r in range(1, rows + 1):
    print("Sum of row", str(r), " = ", sum(table[r-1]))
