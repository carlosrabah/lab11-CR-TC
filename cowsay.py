import sys
from heifer_generator import get_cows
from dragon import Dragon

def list_cows(cows):
    names = [cow.get_name() for cow in cows]
    print("Cows available:", " ".join(names))

def find_cow(name, cows):
    for cow in cows:
        if cow.get_name() == name:
            return cow
    return None

def main():
    cows = get_cows()

    if len(sys.argv) == 1:
        print("Usage:")
        print("python cowsay.py -l")
        print("python cowsay.py MESSAGE")
        print("python cowsay.py -n COW MESSAGE")
        return

    if sys.argv[1] == "-l":
        list_cows(cows)
        return

    if sys.argv[1] == "-n":
        if len(sys.argv) < 4:
            print("Usage: python cowsay.py -n COW MESSAGE")
            return

        cow_name = sys.argv[2]
        message = " ".join(sys.argv[3:])
        cow = find_cow(cow_name, cows)

        if cow is None:
            print(f"Could not find {cow_name} cow!")
        else:
            print(message)
            print(cow.get_image())
            if isinstance(cow, Dragon):
                if cow.can_breath_fire():
                    print("\nThis dragon can breathe fire.")
                else:
                    print("\nThis dragon cannot breathe fire.")
        return

    message = " ".join(sys.argv[1:])
    default_cow = cows[0]
    print(message)
    print(default_cow.get_image())
    if isinstance(default_cow, Dragon):
        if default_cow.can_breath_fire():
            print("\nThis dragon can breathe fire.")
        else:
            print("\nThis dragon cannot breathe fire.")

if __name__ == "__main__":
    main()