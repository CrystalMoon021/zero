
from Obj import Look

def special_check(item):
    if item == "wires":
        Look.unlocked.append("office") #unlock new locations
    else:
        return