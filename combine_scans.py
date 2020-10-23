import os
import csv

from keys import big_ar_keys, decked_keys


def load_file(filename):
    with open(filename, newline="") as f:
        reader = csv.reader(f, delimiter=",")
        imported_list = list(reader)
        return imported_list[1:]


big_ar_files = [
    "more_war_random_rares.csv",
    "misc-3_core_and_misc.csv",
    "simic_vaca.csv",
    "urza.csv",
    "lets_have_a_landfall.csv",
    "chearp_lightning.csv",
]

collection = []
files = os.listdir("scans")
total = 1457
progress = 0
for filename in files:
    file_contents = load_file(f"scans/{filename}")
    for scanned_card in file_contents:
        if filename in big_ar_files:
            keys = big_ar_keys
        else:
            keys = decked_keys

        collection.append(scanned_card)
        progress = len(collection)
        print(f"progress.... {progress}/{total}")
