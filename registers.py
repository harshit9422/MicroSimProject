class Registers:
    def __init__(self):
        self.data = {f"R{i}": 0 for i in range(1, 9)}  # R1 to R8

    def get(self, name):
        return self.data.get(name, 0)

    def set(self, name, value):
        if name in self.data:
            self.data[name] = value

    def display(self):
        print("Register Contents:")
        for reg, val in self.data.items():
            print(f"{reg}: {val}")