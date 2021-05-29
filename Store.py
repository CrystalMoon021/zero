import Inventory
import Look

def arrive_at_Store(cur_place):
    try:
        print("In stock we have: ")
        Look.read_place_items(cur_place)
    except:
        print("The shop is empty")

def buying_items(cur_place, money, item):
    print("Currently you have: $" + str(money))
    Place = Look.read_places_and_stuff()
    try:
        item = item.lower()
        cost = Place[cur_place]["items"][item]["price"]
    except:
        print("You are unable to buy this item")
        return money
    if money > cost:
        money -= cost
        Look.pick_up_item(item, cur_place)
        print("You have brought the " + item)
        return money
    else:
        print("You do not have enough money to buy this item")
        return money