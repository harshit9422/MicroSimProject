class Memory:
    def __init__(self):
        self.mem = {}

    def get(self, address):
        return self.mem.get(address, 0)

    def set(self, address, value):
        self.mem[address] = value

    def dump(self):
        if not self.mem:
            print("No memory used.")
        for address, value in sorted(self.mem.items()):
            print(f"[{address}]: {value}")