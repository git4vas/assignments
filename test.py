stock_level = int(input("Please enter the initial stock level: "))
months = int(input("Please enter the number of month(s) you want to plan: "))
q_m = []
for m in range(months):
    quantity = int(input("Please enter the sales quantity per month: "))
    q_m.append(quantity)
    
#print("Stock Level: ", stock_level)
#print("Planned Month(s): ", months)
#print("Sales Quantity: ", quantity)
planned_m_range = list(range(1,months+1))

for i in planned_m_range:
    #print("Stock: ", stock_level)
    pre_stock_level = stock_level
    if stock_level >= q_m[i-1]:
        production = 0
        stock_level -= q_m[i-1]
    #elif stock_level >= 0 and stock_level < quantity:
    else:
        production = q_m[i-1] - pre_stock_level
        stock_level += production
        stock_level -= q_m[i-1]
    print("Production quantity month 1 -", production)