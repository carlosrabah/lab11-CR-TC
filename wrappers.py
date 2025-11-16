money = int(input("How much money do you have: "))

i = 0

for x in range(1, money+1):
    if x%4 == 0:
        i += 1
    else:
        continue
    if i%3 == 0:
        i +=1

print(f"You can purchase {i} candy bars!")
