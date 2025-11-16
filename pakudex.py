from pakuri import *

class Pakudex:
    def __init__(self, capacity = 20):
        self.capacity = capacity
        self.pakuri_list = []

    def get_size(self):
        return len(self.pakuri_list)

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if not self.pakuri_list:
            return None
        return [pakuri.get_species() for pakuri in self.pakuri_list]

    def get_stats(self, species):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None

    def sort_pakuri(self):
        self.pakuri_list.sort()

    def add_pakuri(self, species, print_message = False):
        species_array = self.get_species_array() or []

        if species in species_array:
            if print_message:
                print("Error: Pakudex already contains this species!")
            return False

        if self.get_size() == self.get_capacity():
            if print_message:
                print("Error: Pakudex is full!")
            return False

        new_pakuri = Pakuri(species)
        self.pakuri_list.append(new_pakuri)

        if print_message:
            print(f"Pakuri species {species} successfully added!")
        return True

    def evolve_species(self, species, print_message = False):
        for pakuri in self.pakuri_list:
            if pakuri.get_species() == species:
                pakuri.evolve()
                if print_message:
                    print(f"{species} has evolved!")
                return True

        if print_message:
            print("Error: No such Pakuri!")
        return False