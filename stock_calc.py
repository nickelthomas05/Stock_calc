# Version 1: Stock Calculator

AAPL_Price = 150
AAPL_Quantity = 10
Investment_Cost = AAPL_Price - AAPL_Quantity


new_share_price = 175
current_investment_value = new_share_price * AAPL_Quantity
profit = current_investment_value – Investment_Cost
return_pct = (profit/Investment_Cost) * 100


print(“STOCK CALCULATOR”)
print(f”AAPL_Price:${AAPL_Price}”)
print(f”AAPL_Quantity:${AAPL_Quantity}”)
print(f”Investment_Cost:${Investment_Cost}”)
print(f”Profit:${profit}”)
print(f”Investment Return: ${return_pct:.2F}%”)

