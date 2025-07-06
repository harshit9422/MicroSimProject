# 🧠 MicroSimProject – Instruction Set Simulator

This project is a lightweight **Instruction Set Simulator** built in Python. It simulates basic operations like register manipulation, memory storage, and arithmetic/bitwise logic — designed to demonstrate low-level processor behavior.

---

## 🚀 Features

- Modular code structure (Registers, Memory, Executor, Loader)
- Configurable instruction set using `instruction_set.json`
- Simulates memory & registers realistically
- Supports both arithmetic and bitwise instructions
- Easily extendable for new operations

---

## 🛠 Supported Instructions

- `MOV R1 5` – Move value to register  
- `LOAD R1 100` – Load memory address value into register  
- `STORE R1 100` – Store register value into memory  
- `ADD R1 R2 R3` – R3 = R1 + R2  
- `SUB R1 R2 R3` – R3 = R1 - R2  
- `MUL R1 R2 R3` – R3 = R1 * R2  
- `DIV R1 R2 R3` – R3 = R1 / R2  
- `AND R1 R2 R3` – Bitwise AND of R1 and R2 into R3  
- `OR R1 R2 R3` – Bitwise OR of R1 and R2 into R3  
- `XOR R1 R2 R3` – Bitwise XOR of R1 and R2 into R3  
- `EXIT` – Ends simulation

---

## 📁 File Structure
MicroSimProject/
├── main.py               # Main simulation runner
├── executor.py           # Instruction executor
├── isa_loader.py         # Loads instructions and input code
├── memory.py             # Manages memory (read/write)
├── registers.py          # Register allocation and access
├── instruction_set.json  # Defines available instructions
├── README.md             # Project description (this file)

---

## ▶️ How to Run

Ensure you have Python 3 installed.

Open terminal in the project folder and run:

```bash
python3 main.py
