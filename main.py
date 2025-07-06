from isa_loader import load_isa
from executor import InstructionExecutor
from memory import Memory
from registers import Registers

def main():
    print("Welcome to MicroSim – Enhanced Edition\n")
    
    instruction_set = load_isa()
    registers = Registers()
    memory = Memory()
    executor = InstructionExecutor(instruction_set, registers, memory)

    print("Enter instructions (type 'EXIT' to quit):")
    while True:
        line = input("> ").strip()
        if line.upper() == 'EXIT':
            break
        if line == "":
            continue
        try:
            executor.execute(line)
        except Exception as e:
            print(f"Error: {e}")

    print("\nFinal Register States:")
    registers.dump()
    print("\nFinal Memory States:")
    memory.dump()

if __name__ == "__main__":
    main()