from Menu import menu

class PlayerCharacter:
    """Picking the traits of the Player class"""
    def __init__(self, name='playerName', race='playerRace'):
        self.hitpoints = 100
        self.inventory= []
        self.name = name
        self.name = input ("What is your name?\n> ")
        self.race = race

    def race_select(self):
        """Selecting the Player Race"""
        print ("Please choose your race: ")
        race_menu = ("Human", "Xeno", "Synthetic")
        selection = menu(race_menu)
        if (selection == 1):
            self.race = 'Human'
        if (selection == 2):
            self.race = 'Xeno'
        if (selection == 3):
            self.race = 'Synthetic'

    def confirm_setup (self):
        """Confirm's Player's Choices"""
        print ("Your name is " + str(self.name) + ". You are a " + str(self.race) + ".")
        print ("You have " + str(self.hitpoints) + " hitpoints. Your inventory is empty.")
        print ("____________________________________________________________________________\n")
	
    def get_name(self):
        """returns player name"""
        return self.name

    def set_name(self, new_name):
        """sets player's name"""
        self.name = new_name

    def get_inventory(self):
        """returns player inventory"""
        return self.inventory

    def set_inventory(self, new_inventory):
        """sets player's inventory"""
        self.inventory = new_inventory

    def add_item(self, new_item):
        self.inventory.append(new_item)
	
    def get_race(self):
        return self.race
    
    def set_race(self, new_race):
        self.race = new_race
    
    def check_inventory(self, item):
        for check_item in self.inventory:
            if check_item == item:
                return True

        return False
	
    
    
	