price = float(input("Enter the price of the item: "))
tax = float(input("Enter the sales tax percentage: "))
tax = tax/100
total = price + price*tax
print(f'Your total is ${total:.2f}')