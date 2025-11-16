def flatten(values):
    if type(values) != list:
        return [values]
    flat_list = []
    for value in values:
        flat_list += flatten(value)
    return flat_list

def mystery1(n):
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    for i in range(n):
        temp=a-c+e
        a=b
        b=c
        c=d
        d=e
        e=temp
    return a

def mystery2(number):
    if number < 10:
        return number
    return number % 10 + mystery2(number // 10)

def collatz_sequence(num):
    print(num, end = " ")

    if num == 1:
        print()
        return
    elif num % 2 == 0:
        return collatz_sequence(num // 2)
    else:
        return collatz_sequence((3 * num) + 1)