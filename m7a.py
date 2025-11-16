def bin(num):
    if num == 0:
        return "0"

    output = ""

    while num != 0:
        output = str(num % 2) + output
        num //= 2
    return output

def capitalize(string):
    word_start = True
    output = ""
    for char in string:
        if char.lower() not in "ousnd" and word_start:
            output += char.upper()
        else:
            output += char.lower()
        word_start = char == " "
    return output

def partition(input_list, partition_size):
    result = []

    for i in range(0, len(input_list), partition_size):
        sublist = input_list[i:i + partition_size]
        result.append(sublist)

    return result