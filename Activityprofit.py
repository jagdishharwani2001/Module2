actual_cost = float(input("Enter the actual amount.."))
sale_amount = float(input("Enter the sale amount..."))
if sale_amount>actual_cost:
    profit = sale_amount - actual_cost
    print("Profit is: ",profit)
else:
    loss = actual_cost - sale_amount
    print("Loss is: ",loss)