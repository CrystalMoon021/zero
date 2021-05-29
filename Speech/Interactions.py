import json

def read_dialogue(): # returns dictionary
    try:
        with open("Speech/Dialogue.json", "r") as file:  # Prep json for reading
            dialogue = json.load(file)  # Read json file convert to dictionary
    except:  # Nothing in inventory: empty file
        dialogue = {}

    return dialogue

def check_for_people(cur_place): # read out ppl in place - part of look cmd
    dialogue = read_dialogue()
    try:
        people = dialogue[cur_place]
        for p in people:
            print(dialogue[cur_place][p]["description"], end=" ")
    except:
        print("There is no one else here.")
        return

def find_person(cur_place, person): # runs when talk to person runs, check if valid person
    s = ""
    person = s.join(person).lower() # process person name
    place = cur_place.lower() # process place name
    dialogue = read_dialogue()
    people_in_place = dialogue[place]
    for key in people_in_place.keys():
        if person.find(key) != -1:
            return place, key
    print("You pause and look around but you cannot find that person here")
    return False, False

def talk_to_person(cur_place, person): # talk to cmd
    dialogue = read_dialogue()
    place, personName = find_person(cur_place, person)

    if personName == False: # person doesn't exist
        return
    else:
        dialogueCount = dialogue[place][personName]["count"] # find how much dialogue to read
        num = 0
        for n in range(dialogueCount): # figure out how much dialogue
            counter = "dialogue" + str(n)
            print(" '" + dialogue[place][personName][counter][num-1] + "' said the " + personName)
            counter = "response" + str(n)
            try: # Incase there is no response just dialogue in json plan
                potentialResponse = dialogue[place][personName][counter]
                print("How would you like to respond? ")
                for response in potentialResponse:
                    print("   " + response)
                while True:
                    try: # check if number
                        num = int(input())
                        print("You responded with: " + dialogue[place][personName][counter][num - 1][2:])
                        break
                    except:
                        print("Please provide a number only")
            except:
                pass # there is no response in database





