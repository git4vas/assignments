sell_list = []
stocks = [
    ["SAP", 106, -3.0],
    ["AAPL", 165, 1.25],
    ["TSLA", 860, 54.2],
    ["ORCL", 76, -0.25],
    ["ZM", 114, 6.2],
    ]

for element in stocks:
    if element[2] > 5:
        sell_list.append(element)
    
print(sell_list)

#list of all the stock symbols with a change of more than +5