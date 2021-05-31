
from Obj import Look
import Commands

def special_check(item, cur_place):
    if item == "wires":
        Look.unlocked.append("office") #unlock new locations
        return cur_place
    elif item == "uniform":
        print("The foundation's collector walks in on you straightening your tie. ")
        print("'What is a guard like you doing here?' he squints in suspicion, 'Are you trying to avoid doing your job?' ")
        print("He ushers you out of the office and opens the front door, 'Go out and do what you're paid for!' he exclaims shoving you out of the building. ")
        Look.unlocked.extend(["church", "house", "store", "town"])
        return "town" # change location to town
    else:
        return cur_place