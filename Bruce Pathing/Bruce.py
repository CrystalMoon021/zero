church = ['town','church basement']
shop = ['town']
house = ['forest','town']
cave = ['forest']
forest = ['cave','house']
townhall = ['town']
churchBasement = ['church']
town = ['house','church','shop','townhall']

currentLocation = 'house'

def travel(destination):
    if(currentLocation == 'church'):
        if(destination == 'town' || destination == 'churchBasement'):
            currentLocation = destination
        else:
            print('You cannot reach the ' + destination + 'from your current location')
    if(currentLocation == 'shop'):
        if(destination == 'town'):
            currentLocation = destination
        else:
            print('You cannot reach the ' + destination + 'from your current location')
    if(currentLocation == 'house'):
        if(destination == 'forest' || destination == 'town'):
            currentLocation = destination
        else:
            print('You cannot reach the ' + destination + 'from your current location')
    if(currentLocation == 'cave'):
        if(destination == 'forest'):
            currentLocation = destination
        else:
            print('You cannot reach the ' + destination + 'from your current location')
    if(currentLocation == 'forest'):
        if(destination == 'cave' || destination == 'house'):
            currentLocation = destination
        else:
            print('You cannot reach the ' + destination + 'from your current location')
    if(currentLocation == 'townhall'):
        if(destination == 'town'):
            currentLocation = destination
        else:
            print('You cannot reach the ' + destination + 'from your current location')
    if(currentLocation == 'churchBasement'):
        if(destination == 'church'):
            currentLocation = destination
        else:
            print('You cannot reach the ' + destination + 'from your current location')
    if(currentLocation == 'town'):
        if(destination == 'shop' || destination == 'house' || destination == 'church' || destination == 'townhall'):
            currentLocation = destination
        else:
            print('You cannot reach the ' + destination + 'from your current location')
    return


        
        
