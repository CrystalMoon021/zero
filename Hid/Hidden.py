import json
from Inv import Inventory


def read_hidden(): # returns dictionary of hidden
    try:
        with open("Hid/Hidden Objects.json", "r") as file:  # Prep json for reading
            hidden = json.load(file)  # Read json file convert to dictionary
    except:  # Nothing in inventory: empty file
        hidden = {}

    return hidden

def write_hidden(hidden): # write dict of hidden
    with open("Hid/Hidden Objects.json", "w") as file:  # Prep json for writing
        json.dump(hidden, file, indent=4, sort_keys=True)  # Rewrite the hidden data back with new items


def hidden_obj_unlocked(item): # when a hidden item is unlocked
    hidden = read_hidden()
    Bag = Inventory.read_inventory()
    itemName = hidden[item]["name"] # item already checked before
    Bag[itemName] = hidden[item]
    Inventory.write_inventory(Bag) # add to inv