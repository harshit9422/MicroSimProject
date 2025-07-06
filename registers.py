class Registers:
    def __init__(self):
        self.reg = {f"R{i}": 0 for i in range(8)}

    def get(self, name):
        return self.reg.get(name.upper(), 0)

    def set(self, name, value):
        self.reg[name.upper()] = value

    def dump(self):
        for name, value in self.reg.items():
            print(f"{name}: {value}")