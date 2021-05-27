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
    person = person.lower()
    place = cur_place.lower()
    people_in_place = dialogue[place]

    pplMatch = False

    for key in people_in_place.keys():
        if person.find(key) != -1:
            personName = key
            pplMatch = True
            break

    if pplMatch == False:
        raise ValueError
    else:
        dialogueCount = len(dialogue[place][personName])-1
        for n in range(int(dialogueCount/2)):
            counter = "dialogue" + str(n)
            print(dialogue[place][personName][counter])
            counter = "response" + str(n)
            potentialResponse = dialogue[place][personName][counter]
            print("How would you like to respond? ")
            for response in potentialResponse:
                print("   " + response)
            try:
                num = int(input())
                print("You responded with: " + dialogue[place][personName][counter][num-1][2:])
            except:
                print("Please provide a number only")

        return




