"""MainStory for itemquest"""

import time
from Menu import menu
from PlayerItem import PlayerItem


def intro_story(player):
    """The intro story for itemquest"""
 #   time.sleep(5)
    print("Your escape pod has crash-landed on a jungle planet. " +
          "Inside your escape pod is a crate filled with items, " +
          "but you can only take one. Which one do you take: ")
    item_menu = ("flashlight", "medkit", "knife")
    selection = menu(item_menu)
    """Presents the player with item selection options"""
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
        PlayerItem.itemName = 'knife'
        player.add_item('knife')
        print ("Your inventory now contains: " +
               str(player.get_inventory()))

    print("After exiting your escape pod, you find yourself knee-deep in " +
          "swampy waters. To the east is a jungle and the sounds of alien " +
          "creatures echo from within. To the west you can see buildings " +
          "in the distance. To the north is more swamp. Which way do you go: ")
    direction_menu = ("east", "west", "north")
    """Presents the player with direction selection options"""
    selection = menu(direction_menu)
    if selection is 1:
        forest_story(player)
    if selection is 2:
        city_story()
    if selection is 3:
        swamp_story()

def forest_story(player):
        """The forest story for itemquest"""
        print("You go east, moving into the jungle at a brisk walk. " +
              "Shortly after passing the tree-line you find yourself " +
              "in near-pitch darkness. Luminescent vegitation provides " +
              "the only light. Do you turn on your flashlight?")
        yn_menu = ("yes", "no")
        selection = menu(yn_menu)
        """asks the player if they want to turn on the flashlight"""
        if (selection == 1):
            if "flashlight" in player.inventory:
                print ("You flick on the flashlight and discover a lurking tentacled creature! " +
                       "Before it can attack you, you manage to step on the creature.")
            if "knife" in player.inventory:
                print ("You go to turn on your flashlight, but you don't have one! A tentacled creature leaps out at you. " +
                      "Remembering that you have a knife, you take it out and stab the beast to death.")
            if "medkit" in player.inventory:
                player.hitpoints -= 10
                print ("You go to turn on your flashlight and realize that you do not have one! " + 
		"A tentacled creature leaps from the darkness and attacks you! You fight it off, but not without taking damage. " +
		"You now have " + str(player.hitpoints) + " hitpoints.")
                player.hitpoints += 10
                print ("Remembering your medkit, you bandage your wounds. You now have " +str(player.hitpoints) + " hitpoints.") 

        if (selection == 2):
            if "flashlight" in player.inventory:
                player.hitpoints -= 10
                print ("You decided not to use the flashlight. While wading through the darkness, a tentacled creature leaps onto your face. " +
                "You manage to fight the creature off, but not without taking damage. " +
                "You now have " + str(player.hitpoints) + " hitpoints.")
            else:
                print ("While wading through the darkness, a tentacled creature leaps onto your face. " +
                "You manage to fight the creature off, but not without taking damage. " +
                "You now have " + str(player.hitpoints) + " hitpoints.")

        print("You make your way further into the jungle. From the shadows, blue-tinted eyes peer at you. Fortunately, none of the creatures attack. " +
              "After walking for what feels like an eternity, you see flames between the trees. In the darkness, the flames are like a beacon. " +
              "Seemingly unable to control your own actions, you walk towards the flames.")

        

# def city_story(player):



# def swamp_story(player):