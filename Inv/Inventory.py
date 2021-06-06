import json
from Inv import ItemEffects
from Obj import Look

import sys, os

# Disable printing
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore printing
def enablePrint():
    sys.stdout = sys.__stdout__


def reset_inventory():
    with open("Inv/Bag reset.json", "r") as file:  # Prep json for reading
        Bag = json.load(file)  # Read json file convert to dictionary
    write_inventory(Bag)

def read_inventory(): # returns dictionary of Bag
    try:
        with open("Inv/Bag.json", "r") as file:  # Prep json for reading
            Bag = json.load(file)  # Read json file convert to dictionary
    except:  # Nothing in inventory: empty file
        Bag = {}

    return Bag

def write_inventory(Bag): # write to inv
    with open("Inv/Bag.json", "w") as file:  # Prep json for writing
        json.dump(Bag, file, indent=4, sort_keys=True)  # Rewrite the inventory back with new items

def print_inventory(): #prints the items in inv (inv cmd)
    Bag = read_inventory()
    print("Currently in your bag you hold: ")
    for key in Bag.keys():
        print("    " + key)

def add_item_to_inventory(itemDict): # input dictionary from Look (not directly from input) for pick up cmd
    Bag = read_inventory()
    Bag[itemDict["name"]] = itemDict  # add a new key and value
    write_inventory(Bag)

def find_item_name_inventory(item): # find if an item exists in inv from input
    s = ""
    item = s.join(item).lower()
    Bag = read_inventory()
    for key in Bag.keys():
        if item.find(key) != -1:
            return key
    print("You see no such item in your inventory")
    return False

def examine_item_in_inventory(examineItem): #x item cmd
    Bag = read_inventory()
    itemName = find_item_name_inventory(examineItem)

    if itemName == False:
        print("You don't see that item nearby either. ")
        return
    else:
        print(Bag[itemName]["examine"])

def wear_item(item, place):
    blockPrint() # avoid printing error msg for looking in inv and places
    itemName = find_item_name_inventory(item)
    cur_place = place

    if itemName == False:
        itemPlaceName, placeName = Look.find_item_name(item, place)  # check if item exists in that place
        enablePrint() # allow print
        if itemPlaceName == False:  # can't find item
            print("I cannot find that item in your inventory or here")
            return cur_place
        else:
            # item in places
            Look.pick_up_item(itemPlaceName, placeName) # will check if store and if in place database again
    cur_place = use_item(itemPlaceName, placeName)  # update cur place based on special effects of item
    return cur_place


def use_item(item, cur_place): # use or break item cmd (for now only break)
    itemName = find_item_name_inventory(item) # check if item exists in inv
    Bag = read_inventory()

    if itemName == False:  # can't find item
        print("Pick up items first, to use items they must be in your inventory. ")
        return cur_place
    else:
        try: # check if can be used
            Bag[itemName]["usePlaces"]
        except:
            print("This item cannot be used")
            return cur_place
        if cur_place not in Bag[itemName]["usePlaces"]:
            print(f"You see nowhere to use the {itemName} in the {cur_place}")
            return cur_place
        else: # successfully used
            print(Bag[itemName]["usedText"][cur_place])
            write_inventory(Bag)
            cur_place = ItemEffects.special_check(itemName, cur_place)  # check for certain things like unlocking locations
            return cur_place

def eat_item(item): # eat item cmd
    if item != []:
        Bag = read_inventory()
        itemName = find_item_name_inventory(item) # check if exists

        if itemName == False:
            print("The item must be in your inventory for you to consume it")
            return
        else:
            try:
                print(Bag[itemName]["eat"])
            except:
                print("I don't think the " + itemName + " would agree with you")
    else:
        print("Indicate what you are eating. ")



