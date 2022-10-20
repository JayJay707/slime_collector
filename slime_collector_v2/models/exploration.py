#!/usr/bin/python3
"""Contains class Exploration"""
from random import choice
from random import randint
from models.base_model import BaseModel
from models.inventory import inventory
from models.inventory import slime_collection
from models.slime import Slime
from models.combat import Combat
from models.player import player


class Exploration(BaseModel):
    """Exploration Class"""

    def __init__(self, region, monster_list):
        """Init"""
        super().__init__()
        self.explore(region, monster_list)

    def explore(self, region, monster_list):
        """Exploring a region"""
        number = randint(0, 10)
        if number == 0:
            print("Sorry, you didn't find anything while exploring :(")
        else:
            result = []
            slimes = []
            i = 1
            while i != number:
                result.append(choice(region.item_list))
                i += 1
            j = 1
            while j != number:
                slime_chance = randint(0,1)
                if slime_chance == 1:
                    slimes.append(Slime())
                j += 1
            for item in result:
                inventory.add(item)
                print("You found a", item.name)
            for slime in slimes:
                slime_collection.add(slime)
                print("You found a", slime.name)
        combat_chance = randint(0, 1)
        monster = choice(monster_list)
        if combat_chance == 1:
            print("You encountered a", monster.name, "!")
            combat = Combat(player, monster)
        else:
            print("You didn't encounter any monster.")
