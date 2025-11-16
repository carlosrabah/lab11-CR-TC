import math

result = 0.0
results_list = []

def calculator():
    global result, results_list

    show_menu = True

    while True:
        if show_menu:
            print(f"""Current Result: {round(result, 2)}

Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average
""")

        selection = int(input("Enter Menu Selection: "))

        if selection == 0:
            print("Thanks for using this calculator. Goodbye!")
            return False

        elif selection < 0 or selection > 7:
            print("Error: Invalid selection!")
            show_menu = False

        elif selection == 7:
            if len(results_list) == 0:
                print("Error: No calculations yet to average!")
            else:
                avg = sum(results_list) / len(results_list)
                print(f"""Sum of calculations: {sum(results_list)}
Number of calculations: {len(results_list)}
Average of calculations: {round(avg, 2)}
""")
            show_menu = False

        else:
            x = input("Enter first operand: ")
            if x == "RESULT":
                operand1 = results_list[-1]
            else:
                operand1 = float(x)
            y = input("Enter second operand: ")
            if y == "RESULT":
                operand2 = results_list[-1]
            else:
                operand2 = float(y)

            if selection == 1:
                result = operand1 + operand2
            elif selection == 2:
                result = operand1 - operand2
            elif selection == 3:
                result = operand1 * operand2
            elif selection == 4:
                result = operand1 / operand2
            elif selection == 5:
                result = operand1 ** operand2
            elif selection == 6:
                result = math.log(operand2, operand1)

            results_list.append(result)
            show_menu = True

calculator()