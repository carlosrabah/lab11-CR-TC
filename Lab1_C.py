import math

year1 = int(input("Enter the year for date 1: "))
month1 = int(input("Enter the month for date 1: "))
day1 = int(input("Enter the day for date 1: "))
year2 = int(input("Enter the year for date 2: "))
month2 = int(input("Enter the month for date 2: "))
day2 = int(input("Enter the day for date 2: "))

year = 12
month = 30

yeardifference = year2 - year1
monthdifference = (yeardifference * 12) + (month2 - month1)
difference = abs((monthdifference * 30) + (day2 - day1))

print(f'The difference between {month1}/{day1}/{year1} and {month2}/{day2}/{year2} is {difference} days!')