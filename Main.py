import Inventory
import Interactions
import Look
import Store

cur_place = "town"
money = 20

print("Welcome to town Zero")

while True:
    print("\nWhat would you like to do now?")

    command = input().lower().split()
    cmd = command[0].lower()

    if cmd == "take" or (command[0] == "pick" and command[1] == "up") or cmd == "grab":
        try:
            s = ""
            if command[0] == "pick" and command[1] == "up":
                Look.pick_up_item(s.join(command[2:]), cur_place)
            else:
                Look.pick_up_item(s.join(command[1:]), cur_place)
            print("You successfully picked up: " + command[-1])
        except:
            print("Huh, I can't find that item here")

    elif cmd == "i" or cmd == "inventory" or cmd == "inv":
        print("Currently in your bag you hold: ")
        Inventory.print_inventory()

    elif cmd == "x" or cmd == "examine" or cmd == "inspect":
        try:
            s = ""
            Inventory.examine_item_in_inventory(s.join(command[1:]))
        except:
            try:
                s = ""
                Look.examine_item_in_place(s.join(command[1:]), cur_place)
            except:
                print("Huh, make sure to indicate which object to examine (e.g, x apple)")

    elif cmd == "l" or cmd == "look" or cmd == "describe":
        Look.read_place_description(cur_place)
        Look.look_around(cur_place)

    elif cmd == "g" or cmd == "go" or cmd == "gt" or cmd == "travel":

        if command[-1] == "store":
            Look.read_place_description(command[-1])
            cur_place = "store"
            print("'What would you like to buy?' asks the shopkeeper")
            Store.arrive_at_Store(cur_place)
        else:
            try:
                Look.read_place_description(command[-1])
                cur_place = command[-1]
            except:
                print("Huh I can't find that place")

    elif cmd == "buy":
        try:
            money = Store.buying_items(cur_place, money, command[1])
        except:
            print("You cannot buy this item")

    elif cmd == "talk":
        #try:
            s = ""
            Interactions.talk_to_person(cur_place, s.join(command[1:]))
        #except:
         #   print("Huh, I can't find that person")

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

    elif cmd == "swear" or cmd == "curse" or cmd == "klag":
        print("You let out a string of curses that would make your Uncle Rogers proud")
    else:
        print("Sorry no such option is available")
