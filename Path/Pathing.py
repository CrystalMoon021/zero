import json
from Obj import Store
from Obj import Look

def path_data_reset():
    with open("Path/Map reset.json", "r") as file:  # Prep json for reading
        Map = json.load(file)  # Read json file convert to dictionary
    write_map(Map)

def write_map(Place):
    with open("Path/Map.json", "w") as file:  # Prep json for writing
        json.dump(Place, file, indent=4, sort_keys=True)  # Rewrite

def read_map():
    with open("Path/Map.json", "r") as file:  # Prep json for reading
        Map = json.load(file)
    return Map

def check_unlocked(cur_place):
    Map = read_map()
    return Map[cur_place]

def unlock_places(cur_place, places):
    Map = read_map()
    for place in places:
        Map[cur_place][place] = True
    write_map(Map)

def travel(destination, cur_place, money):
    Map = read_map()
    try:
        checkPath = Map[cur_place][destination]
        if checkPath == True: # meaning you can get there
            cur_place = destination
            print("You have arrived at: " + cur_place)
            if cur_place == "store": # if store
                Store.arrive_at_Store(cur_place, money)
            else: # if any other location
                Place = Look.read_places_and_stuff()
                print(Place[cur_place]["entry"])
            return cur_place
        elif checkPath == False: # it's possible but right now it's a locked location
            print(Map[cur_place]["locked"])
            return cur_place
    except:
        print("You cannot travel to the " + destination + " from the " + cur_place)
        return cur_place





