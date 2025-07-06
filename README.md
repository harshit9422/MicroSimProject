# MicroSimProject 🧠

A simple **Instruction Set Simulator** built in Python that mimics a minimalist CPU’s memory and register behavior.

## 🚀 Features

- Simulates basic CPU instructions: `LOAD`, `STORE`, `ADD`
- JSON-based instruction input
- Clean modular design with separate files for memory, registers, execution, and parsing
- Easy to extend with more instructions

## 📁 File Structure

| File | Purpose |
|------|---------|
| `main.py` | Entry point, controls execution |
| `isa_loader.py` | Loads and parses JSON instructions |
| `executor.py` | Executes instructions |
| `memory.py` | Handles simulated memory |
| `registers.py` | Simulates CPU registers |
| `instruction_set.json` | Sample instruction list |

## 📜 Sample instruction_set.json

```json
[
  { "opcode": "LOAD", "operands": ["R1", "100"] },
  { "opcode": "LOAD", "operands": ["R2", "104"] },
  { "opcode": "ADD", "operands": ["R3", "R1", "R2"] },
  { "opcode": "STORE", "operands": ["108", "R3"] }
]