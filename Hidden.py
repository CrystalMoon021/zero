import json
import Inventory

def read_hidden(): # returns dictionary of hidden
    try:
        with open("Hidden Objects.json.json", "r") as file:  # Prep json for reading
            hidden = json.load(file)  # Read json file convert to dictionary
    except:  # Nothing in inventory: empty file
        hidden = {}

    return hidden

def write_hidden(hidden):
    with open("Bag.json", "w") as file:  # Prep json for writing
        json.dump(hidden, file, indent=4, sort_keys=True)  # Rewrite the hidden data back with new items



def hidden_obj_unlocked(item):
    hidden = read_hidden()
    bag = Inventory.read_inventory()
    itemName = hidden[item]["name"]
    bag[itemName] = hidden[item][itemName]