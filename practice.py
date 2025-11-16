class Test:
    def __init__(self, name = "Juan", number = 10):
        self.name = name
        self.number = number

    def multiply(self):
        result = len(self.name) * self.number
        print(result)

Test.multiply()