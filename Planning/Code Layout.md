
# Commands
- in the commands.py file it links to all the other functions
- below I have listed the different functions and how they work for people to easier collaborate

## Picking up Items
- Runs the function pick_up_items
Pick_up_items
> Check if item exists in places dict (find_item_name). 
> Moves the item dict it to the bag dict

## Inventory
- Runs the function print_inventory from Inventory.py
> Reads the Bag.json and prints out the items

## Examine Items
- Runs two functions (One for examining items in the place dict and one in the bag dict)
- Check if item exists (find_item_name)
Examine items in place: read the "examine" key for the item in the place dict
Examine items in inventory: read the "examine" key for the item in the bag dict

## Look
- Runs two functions (one reads the "look" description and one runs the look_around function)
> Read_place_description: read the place dict and print the "description" val
Look_around function
- Print out all the object "description"
- Print out the "outside" value for every Place
- Print out the people using the (check_for_people function)
- If the place is the store run a special function (arrive_at_store) to print out the products and ask for money

## Go To Place
- Update the cur_place variable with the name of the new location
- Run the goto_place_entry
Goto_place function
- check if you are already at the place you wanted to go to
- check if the place actually exists in the database  (find_place_name)
- check if the place is somewhere unlocked you can acc go to
- print the "entry" text for the place

## Buy Items
- Make sure you are in the store to be able to buy stuff
Buying_items
- Check if in store (find_item_name)
- Print out the amount of money you have left
- Check if the item exists and can be brought
- Find the cost of the item ("price") and subtract it from the money you have
- Add the item to inventory
- Remove the item from the place database

## Talk to ppl
- Runs the talk_to_person function
Talk_to_person function
- check if person exists (find_person)
- Print out their dialogue (is in list format)
- Print out response options
- Select response option
- Print out responding dialogue (If response[1] then print dialogue[1] ofc the stuff is in lists)

## Break item
- Runs the break_item function
Break_item function
- check if item exists (find_item_name)
- check if the item can be broken (does it have a "brokenText" key)
- print the "brokenText" dialogue
- delete the object from the database - write the new data back into the database
- run the hidden_obj_unlocked function that moves the new object into the inventory

## Use Item
- Runs the use_item function
use_item function
- check if item exists (find_item_name_inventory) if not in inventory tell the user to pick up the item
- check if the item has a "usePlaces" key that indicates it can be used
- check if the current location in a valid location (aka if it's listed in the "usePlaces" list)
- print out the "usedText" dialogue
- run any special effects associated with the item (aka changing the current location, adding new locations to be unlocked)

## Wear Item
- JANICE
- must wear something at any one time
- can wear from place database or inv
- can also reuse the find_item_name function to check if item exists in database
    - you would also need to check if item in inventory using find_item_name_inventory

### Other Functions
- Help: reads the help.txt file and prints it out line by line
- Swear: prints out swear text, dialogue
- Drop: discontinued
- Eat: Check if it's in your inventory, and it it can be eaten print the "eat" dialogue






