from pakudex import *

def display_menu():
    print("\nPakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")

def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    while True:
        capacity_input = input("Enter max capacity of the Pakudex: ")
        try:
            capacity = int(capacity_input)
            if capacity > 0:
                break
            else:
                print("Please enter a valid size.")
        except ValueError:
            print("Please enter a valid size.")

    pakudex = Pakudex(capacity)
    print(f"The Pakudex can hold {capacity} species of Pakuri.")

    running = True
    while running:
        display_menu()
        choice = input("What would you like to do? ")

        if choice == "1":
            species_list = pakudex.get_species_array()
            if species_list is None:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")
                for i, species_name in enumerate(species_list, 1):
                    print(f"{i}. {species_name}")

        elif choice == "2":
            species_name = input("Enter the name of the species to display: ")
            stats = pakudex.get_stats(species_name)
            if stats is None:
                print("Error: No such Pakuri!")
            else:
                print(f"Species: {species_name}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}")

        elif choice == "3":
            if pakudex.get_size() == pakudex.get_capacity():
                print("Error: Pakudex is full!")
            else:
                species_name = input("Enter the name of the species to add: ")
                success = pakudex.add_pakuri(species_name, print_message = True)

        elif choice == "4":
            species_name = input("Enter the name of the species to evolve: ")
            pakudex.evolve_species(species_name, print_message = True)

        elif choice == "5":
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!")

        elif choice == "6":
            print("Thanks for using Pakudex! Bye!")
            running = False

        else:
            print("Unrecognized menu selection!")

if __name__ == "__main__":
    main()