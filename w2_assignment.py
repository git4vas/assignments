sales = []
prod = []
stock = int(input("Please enter an initial stock level: "))
months = int(input("Please enter the number of month to plan: "))

for m in range(months):
    sales_m = int(input("Please enter the planned sales quantity: "))
    sales.append(sales_m)
    delta = stock - sales[m]
    if delta > 0:
        prod.append(0)
    else:
        prod.append(-delta)
    stock = stock - sales[m] + prod[m]

print("The resulting production quantities are: ")
for m in range(months):
    print("Production quantity month", m+1, "-", prod[m])