def execute_instruction(instruction, memory, registers):
    opcode = instruction["opcode"]
    operands = instruction["operands"]

    if opcode == "LOAD":
        reg, addr = operands
        value = memory.get(addr)
        registers.set(reg, value)

    elif opcode == "STORE":
        addr, reg = operands
        value = registers.get(reg)
        memory.set(addr, value)

    elif opcode == "ADD":
        dest, reg1, reg2 = operands
        value = registers.get(reg1) + registers.get(reg2)
        registers.set(dest, value)

    elif opcode == "SUB":
        dest, reg1, reg2 = operands
        value = registers.get(reg1) - registers.get(reg2)
        registers.set(dest, value)

    elif opcode == "MUL":
        dest, reg1, reg2 = operands
        value = registers.get(reg1) * registers.get(reg2)
        registers.set(dest, value)

    elif opcode == "DIV":
        dest, reg1, reg2 = operands
        value = registers.get(reg1) // registers.get(reg2)
        registers.set(dest, value)

    else:
        print(f"Unknown instruction: {opcode}")