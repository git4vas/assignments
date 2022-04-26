stock_level = int(input("Please enter the initial stock level: "))
months = int(input("Please enter the number of month(s) you want to plan: "))
q_m = []

for m in range(months):
    quantity = int(input("Please enter the sales quantity per month: "))
    q_m.append(quantity)
    
for m in range(months):
    if stock_level >= q_m[m]:
        production = 0
    else:
        production = q_m[m] - stock_level
    stock_level += production
    stock_level -= q_m[m]
    print("Production quantity month", m + 1, "-", production)