operation = input("Enter the operation: ")
first_operand = float(input("Enter the first operand: "))
second_operand = float(input("Enter the second operand: "))

if operation == "add":
    result = first_operand + second_operand
elif operation == "sub":
    result = first_operand - second_operand
elif operation == "mul":
    result = first_operand * second_operand
elif operation == "div":
    result = first_operand / second_operand
else:
    print("That is not a valid operation.")

print(f"Result is {round(result, 2)}")