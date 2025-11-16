letters = {
    "A": 10, "a": 10, "B": 11, "b": 11, "C": 12, "c": 12,
    "D": 13, "d": 13, "E": 14, "e": 14, "F": 15, "f": 15
}

def hex_char_decode(digit):
    if digit in letters:
        return letters[digit]
    else:
        return int(digit)

def hex_string_decode(digit):
    i = len(digit) - 1
    result = 0
    for char in digit:
        if char in letters:
            result += letters[char] * (16 ** i)
        else:
            result += int(char) * (16 ** i)
        i -= 1
    return result

def binary_string_decode(binary):
    i = len(binary) - 1
    result = 0
    for char in binary:
        result += int(char) * (2 ** i)
        i -= 1
    return result

def binary_to_hex(binary):
    while len(binary) % 4 != 0:
        binary = "0" + binary

    hex_str = ""
    for num in range(0, len(binary), 4):
        chunk = binary[num:num + 4]
        val = binary_string_decode(chunk)
        if val >= 10:
            hex_str += chr(65 + (val - 10))  # A–F
        else:
            hex_str += str(val)
    return hex_str

while True:
    option = int(input(f"""Decoding Menu
-------------
1. Decode hexadecimal
2. Decode binary
3. Convert binary to hexadecimal
4. Quit
Please enter an option: """))

    if option == 4:
        print("Goodbye!")
        break

    x = input("Please enter the numeric string to convert: ")
    if x[0:2] in ("0x", "0b"):
        x = x[2:]

    if option == 1:
        if len(x) == 1:
            print(f"Result: {hex_char_decode(x)}")
        else:
            print(f"Result: {hex_string_decode(x)}")
    elif option == 2:
        print(f"Result: {binary_string_decode(x)}")
    elif option == 3:
        print(f"Result: {binary_to_hex(x)}")