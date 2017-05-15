"""MainStory for itemquest"""

import time
from Menu import menu
from PlayerItem import PlayerItem


def main_story(player):
    """The main story for itemquest"""
    time.sleep(5)
    print("Your escape pod has crash-landed on a jungle planet. " +
          "Inside your escape pod is a crate filled with items, " +
          "but you can only take one. Which one do you take: ")
    item_menu = ("flashlight", "medkit", "compass")
    selection = menu(item_menu)
    if selection is 1:
        PlayerItem.itemName = 'flashlight'
        player.add_item('flashlight')
        print("Your inventory now contains: " +
              str(player.get_inventory()))
    if selection is 2:
        PlayerItem.itemName = 'medkit'
        player.add_item('medkit')
        print("Your inventory now contains: " +
              str(player.get_inventory()))
    if selection is 3:
        PlayerItem.itemName = 'compass'
        player.add_item('compass')
        print ("Your inventory now contains: " +
               str(player.get_inventory()))

    print("After exiting your escape pod, you find yourself knee-deep in " +
          "swampy waters. To the east is a forest and the sounds of alien " +
          "creatures echo from within. To the west you can see buildings " +
          "in the distance. To the north is more swamp. Which way do you go: ")
    direction_menu = ("east", "west", "north")
    selection = menu(direction_menu)
    if selection is 1:
        print("You go east, moving into the forest at a brisk walk. " +
              "Shortly after passing the tree-line you find yourself " +
              "in near-pitch darkness. Luminescent vegitation provides " +
              "the only light. Do you turn on your flashlight?")
        yn_menu = ("yes", "no")
        selection = menu(yn_menu)
        player.check_inventory("flashlight")
        if (selection == 1):
            if "flashlight" in player.inventory:
                print ("You flick on the flashlight!")
            else:
                player.hitpoints -= 10
                print ("You go to turn on your flashlight and realize that you do not have one! " + 
		"A tentacled creature leaps from the darkness and attacks you! You fight it off, but not without taking damage. " +
		"You now have " + str(player.hitpoints) + " hitpoints.")
        if (selection == 2):
            if "flashlight" in player.inventory:
               	pass 
