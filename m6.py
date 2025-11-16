def fourbonacci(n):
    a, b, c, d = 1, 4, 7, 8

    for num in range(n-1):
        temp = a * 4 + b * 3 + c * 2 + d
        a = b
        b = c
        c = d
        d = temp
    return a

def odd_squares(n):
    k = 0
    number = 1

    while k < n:
        if number ** 0.5 == int(number ** 0.5):
            print(number)
            k += 1
        number += 2

def diamond(h):

    mid = h // 2 + 1

    for i in range(1, mid + 1):
        print(" " * (mid - i), end = "")
        for j in range(1, i * 2):
            print(j, end = "")
        print()

    for i in range(1, h - mid + 1):
        print(" " * i, end = "")
        for j in range(1, (h - 2 * i) + 1):
            print(j, end = "")
        print()