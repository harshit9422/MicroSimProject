from isa_loader import load_instructions
from executor import execute_instruction
from memory import Memory
from registers import Registers

def main():
    print("Instruction Set Simulator started.\n")

    memory = Memory()
    registers = Registers()

    # Initialize memory
    memory.set("100", 5)
    memory.set("104", 10)

    instructions = load_instructions("instruction_set.json")

    for instr in instructions:
        execute_instruction(instr, memory, registers)

    print("\nFinal Register State:")
    registers.display()

    print("\nFinal Memory State:")
    memory.display()

if __name__ == "__main__":
    main()