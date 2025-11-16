price = float(input("Enter the price: "))
black_friday = input("Is it black friday [y/n]: ")

if black_friday == "y":
    price *= 0.6
else:
    pass

coupon = input("Do you have a coupon [y/n]: ")

if coupon == "y":
    price *= 0.95
else:
    pass

discount = input("Do you have an employee discount [y/n]: ")

if discount == "y":
    price *= 0.8
else:
    pass

print(f"The final price is: ${price:.2f}")

