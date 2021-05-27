import json

def read_dialogue(): # returns dictionary
    try:
        with open("Dialogue.json", "r") as file:  # Prep json for reading
            dialogue = json.load(file)  # Read json file convert to dictionary
    except:  # Nothing in inventory: empty file
        dialogue = {}

    return dialogue

def check_for_people(cur_place):
    dialogue = read_dialogue()
    people = dialogue[cur_place]
    for p in people:
        print(dialogue[cur_place][p]["description"])

def talk_to_person(cur_place, person):
    dialogue = read_dialogue()
    personName = person.lower()
    place = cur_place.lower()
    people_in_place = dialogue[place]

    pplMatch = False

    for key in people_in_place.keys():
        if personName.find(key) != -1:
            print(dialogue[place][key]["dialogue1"])
            pplMatch = True
            break

    if pplMatch == False:
        raise ValueError
    else:
        return