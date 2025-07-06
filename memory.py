class Memory:
    def __init__(self):
        self.data = {}

    def get(self, address):
        return self.data.get(address, 0)

    def set(self, address, value):
        self.data[address] = value

    def display(self):
        print("Memory Contents:")
        for addr, val in self.data.items():
            print(f"Address {addr}: {val}")