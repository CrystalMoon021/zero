import json
import Inventory

def read_places_and_stuff(): # returns dictionary of places
    try:
        with open("Places and stuff.json", "r") as file:  # Prep json for reading
            allPlaces = json.load(file)  # Read json file convert to dictionary
    except:  # Nothing in inventory: empty file
        allPlaces = {}

    return allPlaces


def look_around(cur_place):
    Place = read_places_and_stuff()
    print("Nearby you can see: ")
    for key in Place.keys():
        if key != cur_place:
            print("     " + key)

    try:
        read_place_items(cur_place)
    except:
        print("You see nothing out of the ordinary")


def read_place_description(examinePlace):
    Place = read_places_and_stuff()
    placeName = examinePlace.lower()
    print("Arrived at: " + Place[placeName]["description"])


def read_place_items(examinePlace):
    Place = read_places_and_stuff()
    placeName = examinePlace.lower()
    items = Place[placeName]["items"]
    print("There are a few items scattered around...")
    for key in items.keys():
        print("    " + items[key]["description"])


def write_places_and_stuff(Place):
    with open("Places and stuff.json", "w") as file:  # Prep json for writing
        json.dump(Place, file, indent=4, sort_keys=True)  # Rewrite


def pick_up_item(item, place):
    allPlaces = read_places_and_stuff()
    itemName = item.lower()
    place = place.lower()
    items = allPlaces[place]["items"]

    itemMatch = False

    for key in items.keys():
        if itemName.find(key) != -1:
            Inventory.add_item_to_inventory(allPlaces[place]["items"][key])  # add to inventory
            del allPlaces[place]["items"][key]  # remove form places database
            write_places_and_stuff(allPlaces)
            itemMatch = True
            break

    if itemMatch == False:
        raise ValueError
    else:
        return




def drop_item(item, place):
    Place = read_places_and_stuff()
    itemName = item.lower()
    place = place.lower()

    # add item back into place
    Bag = Inventory.read_inventory()

    Place[place]["items"][itemName] = Bag[itemName]
    del Bag[itemName]
    write_places_and_stuff(Place)
    Inventory.write_inventory(Bag)


def examine_item_in_place(item, place): #input name of item in string
    allPlaces = read_places_and_stuff()
    itemName = item.lower()
    place = place.lower()
    items = allPlaces[place]["items"]

    itemMatch = False

    for key in items.keys():
        if itemName.find(key) != -1:
            print(allPlaces[place]["items"][key]["description"])
            itemMatch = True
            break

    if itemMatch == False:
        raise ValueError
    else:
        return