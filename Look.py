import json
import Inventory
import Interactions
import Hidden

def read_places_and_stuff(): # returns dictionary of places
    try:
        with open("Places and stuff.json", "r") as file:  # Prep json for reading
            allPlaces = json.load(file)  # Read json file convert to dictionary
    except:  # Nothing in inventory: empty file
        allPlaces = {}

    return allPlaces


def look_around(cur_place):
    read_place_items(cur_place) # check for items and people
    Interactions.check_for_people(cur_place) # check for people
    print("\n")

    Place = read_places_and_stuff()
    for key in Place.keys(): # check for nearby locations
        if key != cur_place:
            print(Place[key]["outside"], end="")
    print("")



def read_place_description(examinePlace):
    Place = read_places_and_stuff()
    placeName = examinePlace.lower()
    print(Place[placeName]["description"])


def read_place_entry(examinePlace):
    try:
        Place = read_places_and_stuff()
        placeName = examinePlace.lower()
        print(Place[placeName]["entry"])
    except:
        print("You squint your eyes but you can't find " + examinePlace + " anywhere")
        return

def read_place_items(examinePlace):
    Place = read_places_and_stuff()
    placeName = examinePlace.lower()
    try:
        items = Place[placeName]["items"]
        for key in items.keys():
            print("    " + items[key]["description"])
    except:
        return

def write_places_and_stuff(Place):
    with open("Places and stuff.json", "w") as file:  # Prep json for writing
        json.dump(Place, file, indent=4, sort_keys=True)  # Rewrite

def use_break_item(item, place):
    Place = read_places_and_stuff()
    itemName = item.lower()
    placeName = place.lower()
    try:
        items = Place[place]["items"]
        itemMatch = False

        for key in items.keys():
            if itemName.find(key) != -1: # found a match
                itemMatch = True
                broken = Place[placeName]["items"][itemName]["broken"]
                if broken == True:
                    print("The item is already broken")
                    return
                else: # successfully broken
                    Place[placeName]["items"][itemName]["broken"] = True
                    write_places_and_stuff(Place)
                    print(Place[placeName]["items"][itemName]["brokenText"])
                    Hidden.hidden_obj_unlocked(itemName)
                break
        if itemMatch == False:
            print("Huh, I can't find that item here")
        else:
            return
    except:
        print("This item cannot be broken")
        return

def pick_up_item(item, place):
    allPlaces = read_places_and_stuff()
    itemName = item.lower()
    place = place.lower()
    items = allPlaces[place]["items"]

    itemMatch = False

    for key in items.keys():
        if itemName.find(key) != -1:
            if allPlaces[place]["items"][key]["take"] == False:
                print("You cannot pick up this item")
                return
            else:
                Inventory.add_item_to_inventory(allPlaces[place]["items"][key])  # add to inventory
                del allPlaces[place]["items"][key]  # remove form places database
                write_places_and_stuff(allPlaces)
                print("You successfully picked up: " + key)
                itemMatch = True
                break

    if itemMatch == False:
        print("Huh, I can't find that item here")
    else:
        return




# def drop_item(item, place):
#     Place = read_places_and_stuff()
#     itemName = item.lower()
#     place = place.lower()
#
#     # add item back into place
#     Bag = Inventory.read_inventory()
#
#     Place[place]["items"][itemName] = Bag[itemName]
#     del Bag[itemName]
#     write_places_and_stuff(Place)
#     Inventory.write_inventory(Bag) # discontinued


def examine_item_in_place(item, place): #input name of item in string
    allPlaces = read_places_and_stuff()
    itemName = item.lower()
    place = place.lower()
    items = allPlaces[place]["items"]

    itemMatch = False

    for key in items.keys():
        if itemName.find(key) != -1:
            print(allPlaces[place]["items"][key]["examine"])
            itemMatch = True
            return True

    if itemMatch == False:
        return False
