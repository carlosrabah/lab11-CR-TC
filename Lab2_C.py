unit_from = input("Enter the unit you are converting from: ")
unit_to = input("Enter the unit you are converting to: ")
temperature = float(input(f"Enter the temperature in {unit_from}: "))

if unit_from == unit_to:
    convertedtemp = temperature
elif unit_from == "Fahrenheit":
    if unit_to == "Celsius":
        convertedtemp = (temperature - 32) * (5/9)
    else:
        convertedtemp = (temperature - 32) * (5/9) + 273.15
elif unit_from == "Celsius":
    if unit_to == "Fahrenheit":
        convertedtemp = (temperature * 1.8) + 32
    else:
        convertedtemp = (temperature + 273.15)
else:
    if unit_to == "Fahrenheit":
        convertedtemp = (temperature - 273.15) * 1.8 + 32
    else:
        convertedtemp = (temperature - 273.15)

convertedtemp = round(convertedtemp, 1)
print(f"That is {convertedtemp} degrees {unit_to}.")