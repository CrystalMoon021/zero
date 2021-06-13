# input("The guards leave and you are finally able to take action")
# input("You think there might be something useful in this room that can help break you out of your handcuffs")
# input("Take a look around")

import Commands
from Inv import Inventory
from Obj import Look
from Path import Pathing

cur_place = "cell"
money = 20
cur_clothes = ["shirt", "pants"]

Inventory.reset_inventory()
Look.place_data_reset()
Pathing.path_data_reset()

# Testing
cur_place, money, cur_clothes = Commands.basic_commands("break cross", cur_place, money, cur_clothes)
cur_place, money, cur_clothes = Commands.basic_commands("use wires", cur_place, money, cur_clothes)
cur_place, money, cur_clothes = Commands.basic_commands("go to office", cur_place, money, cur_clothes)
cur_place, money, cur_clothes = Commands.basic_commands("pick up uniform", cur_place, money, cur_clothes)
cur_place, money, cur_clothes = Commands.basic_commands("go to cell", cur_place, money, cur_clothes)
cur_place, money, cur_clothes = Commands.basic_commands("wear uniform", cur_place, money, cur_clothes)
cur_place, money, cur_clothes = Commands.basic_commands("wear uniform", cur_place, money, cur_clothes)


# change town to city? - janice
# add check clothing cmd?
# inventory for clothing?
# before wearing check if in cur_clothes
# what if you wear something multiple times - aka wear uniform should be use restricted?
# maybe if you take something off you cannot wear again

while True:
    command = input("> ")
    cur_place, money, cur_clothes = Commands.basic_commands(command, cur_place, money, cur_clothes)
    # print(cur_clothes)
    # print(cur_place)







