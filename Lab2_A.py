sidelength1 = float(input("Side length 1: "))
sidelength2 = float(input("Side length 2: "))
sidelength3 = float(input("Side length 3: "))

if sidelength1 == sidelength2 and sidelength2 == sidelength3:
    print("This is an equilateral triangle!")
elif sidelength1 == sidelength2 or sidelength2 == sidelength3 or sidelength1 == sidelength3:
    print("This is an isosceles triangle!")
else:
    print("This is a scalene triangle!")