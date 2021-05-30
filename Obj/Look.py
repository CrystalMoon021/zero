import json
from Inv import Inventory
from Speech import Interactions
from Hid import Hidden
from Obj import Store


unlocked = ["cell", "bathroom"]

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
    if placeName == False:
        return cur_place
    elif placeName == cur_place: # already in the place
        print("You are already here")
        return cur_place
    elif placeName in unlocked:
        if placeName == "store":
            Store.arrive_at_Store(placeName, money)
            return "store"
        else:
            Place = read_places_and_stuff()
            print(Place[placeName]["entry"])
            return placeName
    else:
        if unlocked == ["cell", "bathroom"]:
            print("You try the door of your cell, it's locked. It seems like you're stuck in here till you can pick the lock.")
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
            broken = Place[placeName]["items"][itemName]["broken"]
        except:
            print("This item cannot be broken")
            return
        if broken == True:
            print("The item is already broken")
            return
        else:  # successfully broken
            Place[placeName]["items"][itemName]["broken"] = True
            try:
                Place[placeName]["items"][itemName]["used"] = True
            except:
                pass
            write_places_and_stuff(Place)
            print(Place[placeName]["items"][itemName]["brokenText"])
            Hidden.hidden_obj_unlocked(itemName) # find the hidden item

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

def drop_item(item, place): # drop item cmd
    itemName = Inventory.find_item_name_inventory(item) # check if exists in inventory
    Bag = Inventory.read_inventory()
    Place = read_places_and_stuff()

    if itemName == False:  # can't find item
        return
    elif place == "store" or place == "church":
        print("'This isn't a dumpster!' You return the item to your inventory. ")
        return
    else:
        Place[place]["items"][itemName] = Bag[itemName] # add item to place database
        del Bag[itemName] # delete item from inv
        write_places_and_stuff(Place)
        Inventory.write_inventory(Bag)  # discontinued function only kept for making testing code easier
        print("You have successfully dropped: " + itemName)

def examine_item_in_place(item, place): #input name of item in string
    s = ""
    Place = read_places_and_stuff()  # repeat code instead of using function just this once to avoid error msg when x item that is not in place but in inv
    itemName = s.join(item).lower()
    placeName = place.lower()
    items = Place[placeName]["items"]

    for key in items.keys():  # look thru the items
        if itemName.find(key) != -1:  # found a match
            itemName = key
            print(Place[placeName]["items"][itemName]["examine"])
            return True

    return False


