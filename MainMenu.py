import StartGame
from Menu import menu


def MainMenu():
    start_menu = ("Start", "Credits", "Exit")
    selection = menu(start_menu)
    if (selection == 1):
        StartGame.StartGame()
MainMenu()
	