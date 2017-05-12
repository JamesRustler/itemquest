#!/usr/bin/env python3
""" game desc"""

from Menu import menu
from MainStory import MainStory
from PlayerCharacter import PlayerCharacter

def init():
	"""Initializes all data needed for game"""


def game_loop():
	"""Game loop"""
	exit_status = False
	while( exit_status==False ):
		#GAME GOES HERE
		# set this to exit - exit_status = True
		main_menu = ("Start", "Credits", "Exit")
		selection = menu(main_menu)
		if (selection == 1):
                        player=PlayerCharacter()
                        player.race_select()
                        player.confirm_setup()
                        MainStory(player)
                        exit_status = True
		if (selection == 2):
			print ("This game was developed by Brian Kordek with generous assistance from Kolby Heacock.")
			exit_status = True
		if (selection == 3):
			exit_status = True
		
def clean_up():
	"""Clean up things"""
	pass


def main():
	init()
	game_loop()
	clean_up()


if __name__ == '__main__':
	main()