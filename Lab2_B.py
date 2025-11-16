income = float(input("Enter your total income this year: "))

if income <= 11600:
    owed_taxes = income * 0.10
elif income <= 47150:
    owed_taxes = 11600 * 0.10 + (income - 11600) * 0.12
elif income <= 100525:
    owed_taxes = 11600 * 0.10 + (47150 - 11600) * 0.12 + (income - 47150) * 0.22
elif income <= 191950:
    owed_taxes = 11600 * 0.10 + (47150 - 11600) * 0.12 + (100525 - 47150) * 0.22 + (income - 100525) * 0.24
elif income <= 243725:
    owed_taxes = 11600 * 0.10 + (47150 - 11600) * 0.12 + (100525 - 47150) * 0.22 + (191950 - 100525) * 0.24 + (income - 191950) * 0.32
elif income <= 609350:
    owed_taxes = 11600 * 0.10 + (47150 - 11600) * 0.12 + (100525 - 47150) * 0.22 + (191950 - 100525) * 0.24 + (243725 - 191950) * 0.32 + (income - 243725) * 0.35
else:
    owed_taxes = 11600 * 0.10 + (47150 - 11600) * 0.12 + (100525 - 47150) * 0.22 + (191950 - 100525) * 0.24 + (243725 - 191950) * 0.32 + (609350 - 243725) * 0.35 + (income - 609350) * 0.37

print(f"You owe ${owed_taxes:.2f} this year.")