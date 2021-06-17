import json

def reset_clothing():
    with open("Inv/Wearing reset.json", "r") as file:  # Prep json for reading
        Wearing = json.load(file)  # Read json file convert to dictionary
    write_clothing(Wearing)

def read_clothing(): # returns dictionary of Wearing
    try:
        with open("Inv/Wearing.json", "r") as file:  # Prep json for reading
            Wearing = json.load(file)  # Read json file convert to dictionary
    except:  # Nothing in clothing: empty file
        Wearing = {}

    return Wearing

def write_clothing(Wearing): # write to inv
    with open("Inv/Wearing.json", "w") as file:  # Prep json for writing
        json.dump(Wearing, file, indent=4, sort_keys=True)  # Rewrite the clothing back with new items

def print_clothing(cur_clothes): #prints the items in inv (inv cmd)
    Wearing = read_clothing()
    print("At the bottom of your bag you put: ")
    for key in Wearing.keys():
        print("    " + key)
    print("Currently you are wearing: ")
    for clothing in cur_clothes:
        print("    " + clothing)

def examine_item_in_clothing(itemName): #part x clothing cmd and Look examine function
    Wearing = read_clothing()
    print(Wearing[itemName]["examine"])

def find_item_name_clothing(item): # find if an clothing exists in inv from input
    s = ""
    item = s.join(item).lower()
    Wearing = read_clothing()
    for key in Wearing.keys():
        if item.find(key) != -1:
            return key
    print("You see no such clothing in your bag")
    return False

