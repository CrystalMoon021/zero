import json

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
        return
    else:
        print(Bag[itemName]["examine"])

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
        print("What are you eating?")



