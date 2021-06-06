import json
from Inv import Inventory
from Speech import Interactions
from Hid import Hidden
from Obj import Store
from Path import Pathing



def place_data_reset():
    with open("Obj/Place reset.json", "r") as file:  # Prep json for reading
        allPlaces = json.load(file)  # Read json file convert to dictionary
    write_places_and_stuff(allPlaces)

def read_places_and_stuff(): # returns dictionary of places
    try:
        with open("Obj/Places and stuff.json", "r") as file:  # Prep json for reading
            allPlaces = json.load(file)  # Read json file convert to dictionary
    except:  # Nothing in inventory: empty file
        allPlaces = {}

    return allPlaces

def write_places_and_stuff(Place):
    with open("Obj/Places and stuff.json", "w") as file:  # Prep json for writing
        json.dump(Place, file, indent=4, sort_keys=True)  # Rewrite


def look_around(cur_place, money): # look cmd
    if cur_place == "store":
        Store.arrive_at_Store(cur_place, money) # for store read items diff than other places
    else:
        read_place_items(cur_place) # check for items and people
    Interactions.check_for_people(cur_place) # check for people
    Place = read_places_and_stuff()
    for key in Place.keys(): # check for nearby locations
        unlocked = Pathing.check_unlocked(cur_place) # only read the unlocked locations
        if key != cur_place and key in unlocked:  # make sure not current location and unlocked
            print(Place[key]["outside"], end="")
    print("")

def read_place_items(examinePlace): # part of look cmd
    Place = read_places_and_stuff()
    placeName = examinePlace.lower() # don't need to check if place exists
    try:
        items = Place[placeName]["items"]
        for key in items.keys():
            try:
                print("    " + items[key]["description"])
            except: # no description
                continue
    except:
        return

def read_place_description(examinePlace): # part of look around cmd
    Place = read_places_and_stuff() # don't need to check if place exists cause we must already be in the place to run look
    placeName = examinePlace.lower()
    print(Place[placeName]["description"])


def find_place_name(input): # check if the place exists
    allPlaces = read_places_and_stuff()
    s = ""
    place = s.join(input).lower()

    for key in allPlaces.keys():
        if place.find(key) != -1:
            return key
    print("Huh, I can't find that place")
    return False

def goto_place_entry(newPlace, cur_place, money): # from the go to cmd, returns new value for cur_place
    placeName = find_place_name(newPlace) # check if place exists in database to go to

    if placeName == False: # place doesn't exist
        return cur_place
    elif placeName == cur_place: # already in the place
        print("You are already here")
        return cur_place
    else: # Place exists
        cur_place = Pathing.travel(placeName, cur_place, money)
        return cur_place


def find_item_name(item, place): # check if that item exists in that place
    s = ""
    Place = read_places_and_stuff()
    itemName = s.join(item).lower()
    placeName = place.lower()
    items = Place[placeName]["items"]

    for key in items.keys():  # look thru the items
        if itemName.find(key) != -1:  # found a match
            return key, placeName
    print("Huh, I can't find that item here")
    return False, False

def break_item(item, place): # use or break item cmd (for now only break)
    itemName, placeName = find_item_name(item, place) # check if item exists
    Place = read_places_and_stuff()

    if itemName == False:  # can't find item
        return
    else:
        try:
            print(Place[placeName]["items"][itemName]["brokenText"])
        except:
            print("This item cannot be broken")
            return
        del Place[placeName]["items"][itemName]  # remove item after broken
        write_places_and_stuff(Place)
        Hidden.hidden_obj_unlocked(itemName)  # find the hidden item

def pick_up_item(item, place): # pick up item cmd
    itemName, placeName = find_item_name(item, place) # check if item exists in that place
    allPlaces = read_places_and_stuff()

    if itemName == False:  # can't find item
        return
    elif place == "store":
        print("'Stop that you thief' exclaimed the shopkeeper. You return the item. ")
        return
    else:
        if allPlaces[placeName]["items"][itemName]["take"] == False:
            print("You cannot pick up this item")
            return
        else:
            Inventory.add_item_to_inventory(allPlaces[placeName]["items"][itemName])  # add to inventory
            del allPlaces[placeName]["items"][itemName]  # remove form places database
            write_places_and_stuff(allPlaces)
            print("You successfully picked up: " + itemName)


def examine_items(item, cur_place):
    Inventory.blockPrint()  # avoid printing error msg for looking in inv and places
    itemName, cur_place = find_item_name(item, cur_place)  # check if item exists in that place

    if itemName == False:
        itemName = Inventory.find_item_name_inventory(item) # check in inventory
        Inventory.enablePrint()  # allow print
        if itemName == False:  # can't find item
            print("I cannot find that item in your inventory or here")
            return
        else:
            # item in inventory
            Inventory.examine_item_in_inventory(itemName)
            return
    # itemName exists in the places
    Inventory.enablePrint()  # allow print again in case it didn't go thru loop
    Place = read_places_and_stuff()
    print(Place[cur_place]["items"][itemName]["examine"])



# def drop_item(item, place): # drop item cmd
#     itemName = Inventory.find_item_name_inventory(item) # check if exists in inventory
#     Bag = Inventory.read_inventory()
#     Place = read_places_and_stuff()
#
#     if itemName == False:  # can't find item
#         return
#     elif place == "store" or place == "church":
#         print("'This isn't a dumpster!' You return the item to your inventory. ")
#         return
#     else:
#         Place[place]["items"][itemName] = Bag[itemName] # add item to place database
#         del Bag[itemName] # delete item from inv
#         write_places_and_stuff(Place)
#         Inventory.write_inventory(Bag)  # discontinued function only kept for making testing code easier
#         print("You have successfully dropped: " + itemName)


