import Inventory
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
            Look.pick_up_item(command[-1], cur_place)    # since pick up is two words - nvm I fixed it (Janice) or i made it worse
            print("You successfully picked up: " + command[-1])
        except:
            print("Huh, I can't find that item here")
    elif cmd == "i" or cmd == "inventory" or cmd == "inv":
        print("Currently in your bag you hold: ")
        Inventory.print_inventory()
    elif cmd == "x" or cmd == "examine" or cmd == "inspect":
        try:
            Inventory.examine_item_in_inventory(command[1])
        except:
            try:
                Look.examine_item_in_place(command[1], cur_place)
            except:
                print("Huh, make sure to indicate which object to examine (e.g, x apple)")
    elif cmd == "l" or cmd == "look" or cmd == "describe":
        print("Currently you are at: " + cur_place)
        Look.read_place_description(cur_place)
        Look.look_around(cur_place)

    elif cmd == "g" or cmd == "go" or cmd == "gt" or cmd == "travel":

        if command[-1] == "store":
            cur_place = "store"
            print("What would you like to buy?")
            Store.arrive_at_Store(cur_place)
        else:
            try:
                print("You have arrived at: ")
                Look.read_place_description(command[-1])
                cur_place = Look.read_place_name(command[-1])
            except:
                print("Huh I can't find that place")

    elif cmd == "buy":
        try:
            money = Store.buying_items(cur_place, money, command[1])
        except:
            print("You cannot buy this item")

    elif cmd == "drop":
        try:
            Look.drop_item(command[1], cur_place)
            print("You have successfully dropped: " + command[1])
        except:
            print("Huh, I can't drop that item here")
    elif cmd == "help":
        print("i: check inventory, x: examine something (must be in inventory), l: look around, gt: go to")
        print("You can also pick up and drop items")
    elif cmd == "swear" or cmd == "curse" or cmd == "klag":
        print("You let out a string of curses that would make your Uncle Rogers proud")