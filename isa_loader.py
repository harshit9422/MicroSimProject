import json

def load_instructions(filename):
    with open(filename, "r") as file:
        return json.load(file)