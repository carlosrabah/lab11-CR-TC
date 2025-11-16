word = input("Enter a word: ")
letter = input("Enter the letter to count: ")

i=0

for x in word:
    if x == letter:
        i+=1
    else:
        continue

print(f"{letter} appears {i} times.")