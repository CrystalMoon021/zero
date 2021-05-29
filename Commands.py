import Inventory
import Interactions
import Look
import Store



def basic_commands(cur_place, money):
    #print("\nWhat would you like to do now?")

    command = input("> ").lower().split()
    cmd = command[0].lower()

    if cmd == "take" or (command[0] == "pick" and command[1] == "up") or cmd == "grab":
        s = ""
        if command[0] == "pick" and command[1] == "up":
            Look.pick_up_item(s.join(command[2:]), cur_place)
        else:
            Look.pick_up_item(s.join(command[1:]), cur_place)

    elif cmd == "i" or cmd == "inventory" or cmd == "inv":
        print("Currently in your bag you hold: ")
        Inventory.print_inventory()

    elif cmd == "x" or cmd == "examine" or cmd == "inspect":
        try:
            s = ""
            Look.examine_item_in_place(s.join(command[1:]), cur_place)
        except:
            s = ""
            Inventory.examine_item_in_inventory(s.join(command[1:]))

    elif cmd == "l" or cmd == "look" or cmd == "describe":
        if cur_place == "store":
            Store.arrive_at_Store(cur_place)
            Interactions.check_for_people(cur_place)  # check for people (not people and items like look_around)
            print("\n")
        else:
            Look.read_place_description(cur_place)
            Look.look_around(cur_place)

    elif cmd == "g" or cmd == "go" or cmd == "gt" or cmd == "travel":
        if command[-1] == cur_place:
            print("You are already here")
        else:
            Look.read_place_entry(command[-1])
            cur_place = command[-1]
        if command[-1] == "store":
            Store.arrive_at_Store(cur_place)

    elif cmd == "buy":
        if cur_place == "store":
            money = Store.buying_items(cur_place, money, command[1])
        else:
            print("You don't see any items you can buy, maybe try a store?")

    elif cmd == "talk":
        s = ""
        Interactions.talk_to_person(cur_place, s.join(command[1:]))


    # elif cmd == "drop":
    #     try:
    #         Look.drop_item(command[1], cur_place)
    #         print("You have successfully dropped: " + command[1])
    #     except:
    #         print("Huh, I can't drop that item here")
    elif cmd == "help":
        print("i: check inventory, x: examine something (must be in inventory), l: look around, gt: go to")
        print("You can also pick up and buy items")
        print("To head somewhere or look close at each location use 'go to <placename>' ")
        print("To talk to someone use 'talk to <person>'")

    elif cmd == "swear" or cmd == "curse" or cmd == "klag":
        print("You let out a string of curses that would make your Uncle Rogers proud")

    elif cmd == "eat":
        if command[1:] != []:
            s = ""
            print("I don't think " + s.join(command[1:]) + " would agree with you")
        else:
            print("What are you eating?")
    else:
        print("Sorry no such option is available")

    return cur_place, money