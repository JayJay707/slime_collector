#!/usr/bin/python3
"""Game"""
from models.exploration import Exploration
from models.inventory import inventory
from models.inventory import slime_collection
from models.regions_items import *
from models.monsters_drops import *
from models.player import player

class Game():
    """Game class"""
    def __init__(self):
        self.tutorial()
        username = str(input("Before playing, please enter a username: "))
        player.set_name(username)
        self.play()

    def play(self):
        """Main function to play the game"""
        while True:
            user_input = str(input()).split()
            if user_input[0] == "quit":
                return False
            elif user_input[0] == "show":
                if user_input[1] == "inventory":
                    inventory.display()
                elif user_input[1] == "slimes":
                    slime_collection.display()
                else:
                    print("Invalid command.")
            elif user_input[0] == "explore":
                self.explore(user_input[1])
            elif user_input[0] == "feed":
                self.feed_slime(user_input[1], user_input[2])
            elif user_input[0] == "name":
                if len(user_input) > 3:
                    print("Please enter a valid name. No whitespace.")
                else:
                    self.name_slime(user_input[1], user_input[2])
            elif user_input[0] == "info":
                for i in slime_collection.inventory:
                    i.info()
            elif user_input[0] == "help":
                self.help()
            elif user_input[0] == "tutorial":
                self.tutorial()
            elif user_input[0] == "pet":
                self.pet_slime(user_input[1])
            elif user_input[0] == "player":
                if user_input[1] == "name":
                    player.set_name(user_input[2])
                elif user_input[1] == "info":
                    player.info()
            else:
                print("Invalid command.")

    def explore(self, region):
        """Function to explore a region"""
        if region == "forest":
            explo = Exploration(forest, forest_monsters)
        elif region == "desert":
            explo = Exploration(desert, desert_monsters)
        elif region == "enchanted_forest":
            explo = Exploration(enchanted_forest, enchanted_forest_monsters)
        elif region == "plains":
            explo = Exploration(plains, plains_monsters)
        elif region == "volcano":
            explo = Exploration(volcano, volcano_monsters)
        elif region == "mountain":
            explo = Exploration(mountain, mountain_monsters)
        elif region == "cave":
            explo = Exploration(cave, cave_monsters)
        elif region == "island":
            explo = Exploration(island, island_monsters)
        else:
            print("Please enter a valid region.")
    
    def feed_slime(self, slime, item):
        """Function to feed slimes"""
        for i, j in enumerate(inventory.inventory):
            if j.name == item:
                item = i
                break
        else:
            i = None

        for k, l in enumerate(slime_collection.inventory):
            if l.name == slime:
                slime = k
                break
        else:
            k = None

        if i == None:
            print("Please enter a valid item.")
        elif k == None:
            print("Please enter a valid slime.")
        else:
            slime_collection.inventory[slime].feed(inventory.inventory[item])
    
    def name_slime(self, slime, name):
        """Function to name slimes"""
        for k, l in enumerate(slime_collection.inventory):
            if l.name == slime:
                slime = k
                break
        else:
            k = None
        
        if k == None:
            print("Please enter a valid slime.")
        else:
            slime_collection.inventory[slime].set_name(name)

    def pet_slime (self, slime):
        """Pet the slime"""
        for k, l in enumerate(slime_collection.inventory):
            if l.name == slime:
                slime = k
                break
        else:
            k = None
        
        if k == None:
            print("Please enter a valid slime.")
        else:
            slime_collection.inventory[slime].pet()
    
    def help(self):
        """Prints info about commands"""
        print("help - provides information about commands")
        print("quit - ends game")
        print("tutorial - displays the tutorial")
        print("explore region_name - launches exploration of a region; current regions are: Forest, Enchanted Forest, Plains, Volcano, Cave, Mountain, Island, Desert. Note: For Enchanted Forest, please write 'enchanted_forest'.")
        print("info - displays information about the slimes in your possession")
        print("show inventory|slimes - shows items or slimes in your possession")
        print("feed slime item - feeds an item to a slime; the names must not contain whitespaces and respect case")
        print("name slime new_name - renames a slime; the names must not contain whitespaces and respect case")
        print("player name new_name - change the player's name; the name must not contain whitespaces")
        print("player info - shows information about the player")
    
    def tutorial(self):
        """Displays the tutorial"""
        print("Welcome to Slime Collector, a game where you can collect and evolve as many slimes as you want!")
        print("To start raising slimes, you'll first need to explore. Try typing 'explore forest' for example. You can see a list of all available regions by typing 'help'. You can also use this command if you're ever lost.")
        print("Now that you've explored the forest, you have collected a few items to feed your slime. Keep exploring until you find a slime. Then, type 'feed slime_name item_name' to feed it. Slimes will evolve after being fed ten times, and they will take on the type of the items they ate. Be careful, once you start feeding a slime an item of a certain type, you can't feed it an item of another type!")
        print("To see the type and evolution status of your slime, just type 'info'. It will display information about all your slimes. If you want to name them, just type 'name slime new_name'.")
        print("To see this tutorial again, type 'tutorial'. Finally, if you want to stop playing, just type 'quit'. Be aware that this game does not have a save function.")
    
if __name__ == "__main__":
    game = Game()
