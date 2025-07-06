import json

def load_isa():
    with open("instruction_set.json", "r") as file:
        return json.load(file)