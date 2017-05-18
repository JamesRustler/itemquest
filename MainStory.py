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
        pass
    if selection is 3:
        pass

def forest_story(player):
    """The forest story for itemquest"""
    print("You go east, moving into the jungle at a brisk walk. " +
          "Shortly after passing the tree-line you find yourself " +
          "in near-pitch darkness. Luminescent vegitation provides " +
          "the only light.")
    if "flashlight" in player.inventory:
        print ("Do you turn on your flashlight?")
        yn_menu = ("yes", "no")
        selection = menu(yn_menu)
        if selection is 1:
            print ("You flick on the flashlight and discover a lurking tentacled creature! " +
                   "Before it can attack you, you manage to step on the creature.")
        if selection is 2:
            player.hitpoints -= 10
            print ("You decide not to use the flashlight. While wading through the darkness, a tentacled creature leaps onto your face. " +
                   "You manage to fight the creature off, but not without taking damage. " +
                   "You now have " + str(player.hitpoints) + " hitpoints.")
    if "knife" in player.inventory:
       print ("A tentacled creature leaps out at you. " +
              "Remembering that you have a knife, you take it out and stab the beast to death. " + 
              "You place one of the creature's tentacles in your inventory.")
       PlayerItem.itemName = 'tentacle'
       player.add_item('tentacle')
       print ("Your inventory now contains: " + str(player.get_inventory()))
    if "medkit" in player.inventory:
       player.hitpoints -= 10
       print ("A tentacled creature leaps from the darkness and attacks you! You fight it off, but not without taking damage. " +
              "You now have " + str(player.hitpoints) + " hitpoints.")
       player.hitpoints += 10
       print ("Remembering your medkit, you bandage your wounds. You now have " +str(player.hitpoints) + " hitpoints.") 
    print("You make your way further into the jungle. From the shadows, blue-tinted eyes peer at you. Fortunately, none of the creatures attack. " +
          "After walking for what feels like an eternity, you see flames between the trees. In the darkness, the flames are like a beacon. " +
          "Seemingly unable to control your own actions, you walk towards the flames.")
    print("The flames are coming from the wreckage of a crashed vehicle. Shards of glass and metal are strewn about the area. " + 
          "The main body of the vehicle is engulfed in flame. A short distance from the fire lies a humanoid form. Do you approach it?")
    yn_menu = ("yes", "no")
    selection = menu(yn_menu)
    """asks the player yes or no"""
    if selection is 1:
        print ("You approach the supine form. After kicking it with your boot, the form remains motionless. Do you search the body for useful items?")
        yn_menu = ("yes", "no")
        selection = menu(yn_menu)
        if selection is 1:
            print ("You search the body, finding a small pistol-like weapon. On the side is stenciled: PARTICLE BEAM PROTOYPE - HANDLE WITH CAUTION. It seems this is a prototype beam weapon. Do you take it?")
            yn_menu = ("yes", "no")
            selection = menu(yn_menu)
            if selection is 1: 
                print ("You take the weapon, placing it in your inventory.")
                PlayerItem.itemName = 'beam weapon'
                player.add_item('beam weapon')
                print ("Your inventory now contains: " + str(player.get_inventory()))        
            if selection is 2: 
                print ("You leave the beam weapon where you found it. It looks unstable.")
        if selection is 2: 
            print ("You leave the body alone.")
    if selection is 2:
        print ("You leave the body alone.")
    print ("To your right you hear the rustling of leaves. Someone is approaching. What do you do?") 
    action_menu = ("run", "hide", "fight")
    selection = menu(action_menu)
    if selection is 1: 
        print ("You turn and run as fast as you can.")
        if "flashlight" in player.inventory:
            print ("As you run, the flashlight lights your way, but also reveals your position. You can feel yourself being chased. " + 
                   "You look back to see your pursuer, only to see a group of 3 humanoid figures streaking through the darkness. " + 
                   "You start running faster as the panic grips your mind. After running for what seems like an eternity, the sound of footsteps behind you fades away and you find yourself alone once again.")
        elif "knife" or "medkit" in player.inventory:
            player.hitpoints -= 50
            print ("You stumble through the darkness, unable to see more than mere inches in front of your face. In your blindness you trip and fall into a deep hole in the ground. The fall injures you severely. You now have " + str(player.hitpoints) + " hitpoints.")
            if "medkit" in player.inventory:
                print ("You patch yourself up using the medkit, using the entirety of the medical supplies within.")
                player.hitpoints += 50
                player.remove_item('medkit')
                print ("Your inventory now contains: " + str(player.get_inventory()))
                print ("You now have " + str(player.hitpoints) + " hitpoints.")
            else:
                pass








