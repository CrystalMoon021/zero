
from Obj import Look
from Obj import Diary
from Path import Pathing
from Hid import Hidden
from Inv import Inventory
import Commands

wiresUnlock = ["office"]
uniformUnlock = ["church", "house", "store", "town"]

def special_check(item, cur_place): # return new location to update cur_place
    if item == "wires":
        Pathing.unlock_places(cur_place, wiresUnlock) #unlock new locations
        return cur_place
    elif item == "uniform":
        print("The foundation's lead guard walks in on you straightening your tie. ")
        print("'What is a guard like you doing here?' he squints in suspicion, 'Are you trying to slack off?' ")
        Bag = Inventory.read_inventory()
        try:
            pen = Bag["pen"]
        except:
            print("'This isn't your personal quarters! Pick up your belongings' he picks up the pen and slaps it onto your hand.")
            Hidden.hidden_obj_unlocked("pen")

        print("He ushers you out of the office and opens the front door, 'Go out and do what you're paid for!' he exclaims shoving you out of the building. ")
        Pathing.unlock_places(cur_place, uniformUnlock)
        cur_place = "town" # change location to town
        return cur_place
    elif item == "pen":
        Diary.write_in_diary("diary", cur_place)
        return cur_place