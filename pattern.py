height = int(input("Height: "))
numbers = []
i = 0

for x in range(height):
    i += 1
    numbers.append(i)
    for y in range((height-i)):
        print(' ', end='')
    print(*numbers, sep='')