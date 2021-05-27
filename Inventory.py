import json


def read_inventory(): # returns dictionary of Bag
    try:
        with open("Bag.json", "r") as file:  # Prep json for reading
            Bag = json.load(file)  # Read json file convert to dictionary
    except:  # Nothing in inventory: empty file
        Bag = {}

    return Bag

def write_inventory(Bag):
    with open("Bag.json", "w") as file:  # Prep json for writing
        json.dump(Bag, file, indent=4, sort_keys=True)  # Rewrite the inventory back with new items

def print_inventory(): #prints the items
    Bag = read_inventory()
    for key in Bag.keys():
        print("    " + key)

def add_item_to_inventory(item): # input dictionary
    Bag = read_inventory()
    Bag[item["name"]] = item  # add a new key and value
    write_inventory(Bag)


def examine_item_in_inventory(examineItem): #input name of item in string
    Bag = read_inventory()
    itemName = examineItem.lower()
    itemMatch = False

    for key in Bag.keys():
        if itemName.find(key) != -1:
            print(Bag[key]["description"])
            itemMatch = True
            break

    if itemMatch == False:
        raise ValueError
    else:
        return





