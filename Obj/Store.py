from Obj import Look
from Inv import Inventory


def arrive_at_Store(cur_place, money):
    if money == None:
        money = 0
    try:
        print("In stock we have: ")
        Look.read_place_items(cur_place)
        print("Currently you have: $" + str(money))
    except:
        print("The shop is empty")

def buying_items(cur_place, money, item):
    print("Currently you have: $" + str(money))
    allPlaces = Look.read_places_and_stuff() # get database of place items
    itemName, placeName = Look.find_item_name(item, cur_place)

    if money == None:
        money = 0

    if itemName == False:
        return money
    else:
        cost = allPlaces[placeName]["items"][itemName]["price"]
        if money > cost:
            money -= cost # buy item
            Inventory.add_item_to_inventory(allPlaces[placeName]["items"][itemName])  # add to inventory
            del allPlaces[placeName]["items"][itemName]  # remove form places database
            Look.write_places_and_stuff(allPlaces)
            print("You have brought the " + itemName)
            print("Now you have: $" + str(money))
            return money
        else:
            print("You do not have enough money to buy this item")
            return money