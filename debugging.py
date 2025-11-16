height = int(input("Enter the number of rows (3 - 9): "))
mid = height//2 + 1

for i in range(1, mid + 1):
    print(" " * (mid - i), end = "")
    for j in range(1, i * 2):
        print(j, end = "")
    print()