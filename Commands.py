from Inv import Inventory
from Speech import Interactions
from Obj import Look, Store, Diary


def basic_commands(command, cur_place, money):
    #print("\nWhat would you like to do now?")

    command = command.lower().split()
    try:
        cmd = command[0].lower()
    except: # they just pressed enter blank
        print("You gotta tell me what to do here bud. Don't just leave me hanging. ")
        return cur_place, money

    if cmd == "take" or (command[0] == "pick" and command[1] == "up") or cmd == "grab":
        Look.pick_up_item(command[1:], cur_place)

    elif cmd == "i" or cmd == "inventory" or cmd == "inv":
        Inventory.print_inventory()

    elif cmd == "x" or cmd == "examine" or cmd == "inspect":
        stateInPlace = Look.examine_item_in_place(command[1:], cur_place)
        if stateInPlace != True:
            Inventory.examine_item_in_inventory(command[1:])

    elif cmd == "l" or cmd == "look" or cmd == "describe":
        Look.read_place_description(cur_place)
        Look.look_around(cur_place, money)

    elif cmd == "g" or cmd == "go" or cmd == "gt" or cmd == "travel" or cmd == "goto":
        cur_place = Look.goto_place_entry(command[1:], cur_place, money)

    elif cmd == "buy":
        if cur_place == "store":
            money = Store.buying_items(cur_place, money, command[1:])
        else:
            print("You don't see any items you can buy, maybe try a store?")

    elif cmd == "talk":
        Interactions.talk_to_person(cur_place, command[1:])

    elif cmd == "break":
        Look.break_item(command[1:], cur_place)

    elif cmd == "use":
        cur_place = Inventory.use_item(command[1:], cur_place)

    elif cmd == "wear" or (command[0] == "put" and command[1] == "on"):
        cur_place = Inventory.wear_item(command[1:], cur_place)

    elif cmd == "help":
        f = open("help.txt", "r")
        for line in f:
            print(line, end="")
        print("")

    elif cmd == "swear" or cmd == "curse" or cmd == "klag":
        print("You let out a string of curses that would make your Uncle Rogers proud")

    elif cmd == "eat":
        Inventory.eat_item(command[1:])

    elif cmd == "write":
        Diary.write_in_diary(command[1:], cur_place)

    else:
        print("Sorry no such option is available")

    return cur_place, money



# elif cmd == "drop":
#     Look.drop_item(command[1:], cur_place)