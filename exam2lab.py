def print_backwards(s):
    if s == "":
        return
    print(s[-1], end="")
    print_backwards(s[:-1])

def format_names(names):
    if not names:
        return []

    current = names[0]

    if "," in current:
        formatted = current
    else:
        first, last = current.split()
        formatted = last + ", " + first

    return [formatted] + format_names(names[1:])

def sum_a(data):
    if not data:
        return 0

    current = data[0]
    value = current["a"] if "a" in current else 0

    return value + sum_a(data[1:])

def process_list(numbers):
    if not numbers:
        return []

    evens = [str(numbers[i]) for i in range(0, len(numbers), 2)]

    odds = [numbers[i] * 10 for i in range(1, len(numbers), 2)]

    return evens + odds