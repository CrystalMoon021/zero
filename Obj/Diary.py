from Obj import Look
from Inv import Inventory

def write_in_diary(item, cur_place):
    itemName, cur_place = Look.find_item_name(item, cur_place)
    Bag = Inventory.read_inventory()
    if itemName != "diary": # check if right item
        print("Sorry you can only write in your diary in your cell")
        return
    else:
        try:
            Bag["pen"] # check if you have a pen in your inventory
        except:
            print("You need to find something you can use to write in your diary")
            return

        f = open("Obj/Saved Diary.txt", "r")
        diaryTxt = f.readlines()
        print("\n+++++++ENTRY START+++++++")
        for line in diaryTxt:
            print(line, end="")
        print("\n++++++++ENTRY END++++++++\n")

        f = open("Obj/Saved Diary.txt", "a")
        txt = input("Add a line to your diary: ")

        f.write("\n" + txt)
        f.close()
        print("Diary Entry Saved")

