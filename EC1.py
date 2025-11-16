adultticket = 12.45
kidticket = 9.68

print("""Available movies today:
A)12 Strong:	1)2:30	2)4:40	3)7:50	4)10:50
B)Coco:		1)12:40	2)3:45
C)The Post:	1)12:45	2)3:35	3)7:05	4)9:55
""")

choice = input("Movie choice:   ")

while True:

    if choice != "A" and choice != "B" and choice != "C":
        print("Invalid option; please restart app...")
        break

    showtime = int(input("Showtime:       "))

    if (choice == "A" or choice == "C") and (showtime > 4 or showtime < 0):
        print("Invalid option; please restart app...")
        break
    elif choice =="B" and (showtime > 2 or showtime < 0):
        print("Invalid option; please restart app...")
        break

    numofadult = int(input("Adult tickets:  "))

    if numofadult < 0 or numofadult > 30:
        print("Invalid option; please restart app...")
        break

    numofkids = int(input("Kid tickets:    "))

    if numofkids < 0 or numofkids > 30:
        print("Invalid option; please restart app...")
        break
    elif numofadult + numofkids > 30:
        print("Invalid option; please restart app...")
        break

    if choice == "B" or choice == "C":
        if showtime == 1:
            adultticket = 11.17
            kidticket = 8.00

    total = numofadult * adultticket + numofkids * kidticket

    print(f"Total cost:     ${total:.2f}")
    break