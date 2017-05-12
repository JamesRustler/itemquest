from Menu import menu
from PlayerCharacter import PlayerCharacter
from PlayerItem import PlayerItem
import time


def MainStory (player):
    time.sleep(5) 
    print ("Your escape pod has crash-landed on a jungle planet. Inside your escape pod is a crate filled with items, but you can only take one. Which one do you take: ")
    item_menu = ("flashlight", "medkit", "compass")
    selection = menu(item_menu)
    if (selection == 1):
        PlayerCharacter.get_inventory
        PlayerItem.itemName = 'flashlight'
        player.add_item ('flashlight')
        print ("Your inventory now contains: " + str(player.get_inventory()))

    if (selection == 2):
        PlayerCharacter.get_inventory
        PlayerItem.itemName = 'medkit'
        player.add_item ('medkit')
        print ("Your inventory now contains: " + str(player.get_inventory()))
    
    if (selection == 3):
        PlayerCharacter.get_inventory
        PlayerItem.itemName = 'compass'
        player.add_item ('compass')
        print ("Your inventory now contains: " + str(player.get_inventory()))
    
    print ("After exiting your escape pod, you find yourself knee-deep in swampy waters. To the east is a forest and the sounds of alien creatures echo from within. To the west you can see buildings in the distance. To the north is more swamp. Which way do you go: ")
    direction_menu = ("east", "west", "north")
    selection = menu(direction_menu)
    if selection == 1: 
        print ("You go east, moving into the forest at a brisk walk. Shortly after passing the tree-line you find yourself in near-pitch darkness. Luminescent vegitation provides the only light.")
        yn_menu = ("yes", "no")
        selection = menu(yn_menu)
        player.check_inventory("flashlight")
        if (selection == 1): 
            if player.check_inventory is True:
                print ("You flick on the flashlight!")
            if player.check_inventory is False:
                print ("Booooo")

