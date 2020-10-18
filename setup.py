import json

with open("AllPrintings.json", "r") as f:
    all_printings = json.load(f)

    print(len(all_printings))
