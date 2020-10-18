import os
import csv
import sys

# from keys import (B_CONDITION, B_FOIL, B_LANGUAGE, B_NAME, B_PURCHASE_DATE,
# B_PURCHASE_PRICE, B_QTY, B_SET, B_SET_CODE, D_COLOR, D_COST,
# D_FOIL_PRICE, D_FOIL_QTY, D_MVID, D_NAME, D_NOTES, D_PRICE,
# D_PRICE_SOURCE, D_QTY, D_RARITY, D_REG_QTY, D_SET,
# D_TOTAL_PRICE, D_TYPE)
from keys import big_ar_keys, decked_keys
from mtgsdk import Card, Changelog, Set, Subtype, Supertype, Type


def get_headers(filename):
    with open(filename, newline="") as f:
        reader = csv.reader(f, delimiter=",")
        return list(reader)[0]


def load_file(filename):
    with open(filename, newline="") as f:
        reader = csv.reader(f, delimiter=",")
        imported_list = list(reader)
        return imported_list[1:]


def locate(card):
    pass


def menu():
    i = None
    while i != "q":
        i = input("\n>")
        if i == "f":
            print("find")


def doihave(name, collection):
    res = []
    for i, card in enumerate(collection):
        if (
            name.lower() in card[decked_keys["name"]].lower()
            or name.lower() in card[big_ar_keys["name"]].lower()
        ):
            res.append(card)
    return res


def get_all_in_colors(colors):
    res = []
    for i, card in enumerate(collection):
        for color in colors:
            if color in card[decked_keys["color"]]:
                res.append(card)
            elif len(card) == 9:
                c = card_from_big_ar(card)
                try:
                    if color in c.color:
                        res.append(c)
                except AttributeError:
                    print(card)
                    return

    return res


def lookup_set(set_name):
    s = Set.where(name=set_name)
    for set in s:
        if len(set["code"]) == 3:
            return set


# def card_from_decked(scan_line):
#     name = scan_line[decked_keys["name"]]
#     set_code = lookup_set(scan_line[decked_keys["set"]])
#     return Card.where(name=)


def card_from_big_ar(scan_line):
    print("card from big ar", scan_line)
    name = scan_line[big_ar_keys["name"]]
    set_code = scan_line[big_ar_keys["set_code"]]
    print(f"scanning for card named {name} in set {set_code}")
    c = Card.where(name=name).where(set=set_code).all()
    print(c)
    return c


# def get_

# color = sys.argv[1]
# cards = Card.where(name="opt,negate").all()
# print(cards)


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

        # c = (
        #     Card.where(name=scanned_card[keys["name"]])
        #     .where(setName=scanned_card[keys["set"]])
        #     .all()
        # )
        # if len(c) > 1:
        #     raise Exception("returned multiple cards")
        # c = c[0]
        collection.append(scanned_card)
        progress = len(collection)
        print(f"progress.... {progress}/{total}")


# for card in collection:
#     c = Card.find(card[MVID])
#     print(c)

# for card in collection:
#     print(card)
