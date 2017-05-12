from PlayerCharacter import PlayerCharacter
from PlayerItem import PlayerItem
from Menu import menu
player=PlayerCharacter()

def Confirm_Setup ():
    print ("You are a " + str(player.race) + ".")
    print ("Your name is " + str(player.name) + ". You are a " + str(player.race) + ".")
    print ("You have " + str(player.hitpoints) + " hitpoints. Your inventory contains " + str(player.inventory))

def MainStory (): 
    print ("Your escape pod has crash-landed on a jungle planet. Inside your escape pod is a crate filled with items, but you can only take one: ")
    race_menu = ("flashlight", "medkit", "compass")
    selection = menu(race_menu)
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



Confirm_Setup()
MainStory()