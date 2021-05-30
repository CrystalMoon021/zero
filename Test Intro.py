# print("The guards leave and you are finally able to take action")
# print("You think there might be something useful in this room that can help break you out of your handcuffs")
# print("Take a look around")

import Commands

cur_place = "cell"
money = 20
status = "locked"

#
# def Test():
#     assert 2 + 2 == 5
#
# Test()

while status == "locked":
    cur_place, money = Commands.basic_commands(cur_place, money)







