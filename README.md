# Zero
Our game

## Current Tasks for Coding

Ariel's Quest
- figure out to properly have branches and pull requests on github

Pathing
- e.g, The only way to get to the church's basement is thru the church
- find out some way to do the pathing (list in lists? mapping it somehow?)
- mapping out the connections between locations
> seperate and doesn't interfere with other aspects (the look command searchs in the place json file based on name, as long as there are no repeating place names it'll work)

Shop - DONE
- Have a independent shop inventory json file (maybe have it seperate from the place json files?)
- buy items from the shop (if you have enough money)
- subtract money and add items to inventory, (subtract items from shop?)
> interacts with the inventory


Dialogue
- spit out set dialogue from the txt or json or whatever file for each character
- have the set dialogue for the main protagonist to respond with (3 options to choose from with 1, 2, 3)
- as for the rest idk, try to figure it out
- maybe some way to map out the dialogue (e.g, if you come back to the priest twice it's different dialogue)
> prob need to wait for the story to get more clear

Fighting - Optional (do it if you like to or have extra time ig)
- free reins
- maybe something like kingdom of loathing style?
- we might not have any fighting at all
- would there be things to equip? what stats to consider?

Descriptions
- for item descriptions, list them when LOOKING

I'd like to go from this:
```
Currently you are at: house # delete this because it is redundant with the line below
A creaky old house 
Nearby you can see: # make this into a description of available locations, if places are unlockable use optional message
     church
     store
     town
     
# maybe don't print this every time but idk broooo
To head somewhere or look close at each location use 'go to <placename>' 
You see a few rocks and... # consistent object descriptions
    key
    snail
```

to maybe something like this, if possible:
not sure if this is entirely a good idea since it's harder to pick out the locations, but also more stylistic imo
```
A creaky old house with no door. There are spiderwebs on the windowsill.

From here, the dirt trail outside leads back to the store and town. The church looms in the distance. 

# for example, if we unlock an attic it'll be separate
The ladder leading up to the attic is quickly collecting dust. 

A key is lying on the kitchen counter. I can see a rather large snail on the wall.
```

thoughts?

## Current Tasks for Story

Name
Plot
Map
Characters

