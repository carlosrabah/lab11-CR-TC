class ElectronicDevice:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Laptop(ElectronicDevice):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def display_info(self):
        super().display_info()
        print(f"Battery Life: {self.battery_life} hours")