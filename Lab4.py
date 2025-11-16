def fibonacci(z):
    num_list = [0, 1]
    x = 0
    y = 1

    if z == 1:
        result = 0
    elif z == 2:
        result = 1
    else:
        for num in range(z-2):
            result = num_list[x] + num_list[y]
            num_list.append(result)
            x += 1
            y += 1
    return result

def is_prime(N):
    if N < 2:
        return False
    elif N == 2:
        return True
    else:
        for x in range(2, N):
            if N % x == 0:
                return False
        return True

def print_prime_factors(total):
    original_total = [total]
    factor = 2
    factors = []

    while True:
        if total == 1:
            break
        elif total % factor == 0:
            factors.append(factor)
            total /= factor
        elif total % factor != 0:
            factor += 1

    for i, value in enumerate(factors):
        if i == 0:
            print(f"{original_total[0]} = {value}", end=" ")
        else:
            print(f"* {value}", end = " ")