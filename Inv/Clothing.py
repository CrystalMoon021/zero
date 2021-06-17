# import json
#
# def reset_clothing():
#     with open("Inv/Wearing reset.json", "r") as file:  # Prep json for reading
#         Wearing = json.load(file)  # Read json file convert to dictionary
#     write_clothing(Wearing)
#
# def read_clothing(): # returns dictionary of Wearing
#     try:
#         with open("Inv/Wearing.json", "r") as file:  # Prep json for reading
#             Wearing = json.load(file)  # Read json file convert to dictionary
#     except:  # Nothing in clothing: empty file
#         Wearing = {}
#
#     return Wearing
#
# def write_clothing(Wearing): # write to inv
#     with open("Inv/Wearing.json", "w") as file:  # Prep json for writing
#         json.dump(Wearing, file, indent=4, sort_keys=True)  # Rewrite the clothing back with new items
#
# def print_clothing(cur_clothes): #prints the items in inv (inv cmd)
#     Wearing = read_clothing()
#     print("At the bottom of your bag you put: ")
#     for key in Wearing.keys():
#         print("    " + key)
#     print("Currently you are wearing: ")
#     for clothing in cur_clothes:
#         print("    " + clothing)
#
# def examine_item_in_clothing(itemName): #part x clothing cmd and Look examine function
#     Wearing = read_clothing()
#     print(Wearing[itemName]["examine"])
#
# def find_item_name_clothing(item): # find if an clothing exists in inv from input
#     s = ""
#     item = s.join(item).lower()
#     Wearing = read_clothing()
#     for key in Wearing.keys():
#         if item.find(key) != -1:
#             return key
#     print("You see no such clothing in your bag")
#     return False
#
# #
# # def examine_items(item, cur_place):
# #     Inventory.blockPrint()  # avoid printing error msg for looking in inv and places
# #     itemName, cur_place = find_item_name(item, cur_place)  # check if item exists in that place
# #
# #     if itemName == False:
# #         itemName = Clothing.find_item_name_clothing(item) # check in clothing
# #         if itemName == False:
# #             itemName = Inventory.find_item_name_inventory(item) # check in inventory
# #             Inventory.enablePrint()  # allow print
# #             if itemName == False:  # can't find item
# #                 print("I cannot find that item in your inventory or here")
# #                 return
# #             else:
# #                 # item in inventory
# #                 Inventory.examine_item_in_inventory(itemName)
# #                 return
# #         else:
# #             # item in clothing
# #             Inventory.enablePrint()  # allow print
# #             Clothing.examine_item_in_clothing(itemName)
# #             return
# #     # itemName exists in the places
# #     Inventory.enablePrint()  # allow print again in case it didn't go thru loop
# #     Place = read_places_and_stuff()
# #     print(Place[cur_place]["items"][itemName]["examine"])