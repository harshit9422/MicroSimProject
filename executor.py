class InstructionExecutor:
    def __init__(self, instruction_set, registers, memory):
        self.instruction_set = instruction_set
        self.registers = registers
        self.memory = memory

    def execute(self, line):
        parts = line.strip().split()
        if not parts:
            return

        op = parts[0].upper()
        operands = parts[1:]

        if op == "MOV":
            self.registers.set(operands[0], int(operands[1]))
        elif op == "LOAD":
            self.registers.set(operands[0], self.memory.get(int(operands[1])))
        elif op == "STORE":
            self.memory.set(int(operands[1]), self.registers.get(operands[0]))
        elif op == "ADD":
            self.registers.set(operands[0], self.registers.get(operands[1]) + self.registers.get(operands[2]))
        elif op == "SUB":
            self.registers.set(operands[0], self.registers.get(operands[1]) - self.registers.get(operands[2]))
        elif op == "MUL":
            self.registers.set(operands[0], self.registers.get(operands[1]) * self.registers.get(operands[2]))
        elif op == "DIV":
            divisor = self.registers.get(operands[2])
            if divisor == 0:
                raise ZeroDivisionError("Division by zero")
            self.registers.set(operands[0], self.registers.get(operands[1]) // divisor)
        elif op == "AND":
            self.registers.set(operands[0], self.registers.get(operands[1]) & self.registers.get(operands[2]))
        elif op == "OR":
            self.registers.set(operands[0], self.registers.get(operands[1]) | self.registers.get(operands[2]))
        elif op == "XOR":
            self.registers.set(operands[0], self.registers.get(operands[1]) ^ self.registers.get(operands[2]))
        else:
            raise ValueError(f"Unsupported operation: {op}")