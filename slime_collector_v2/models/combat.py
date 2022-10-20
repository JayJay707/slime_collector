#!/usr/bin/python3
"""Contains class Combat"""
from models.base_model import BaseModel
from random import randint
from random import choice
from models.inventory import inventory


class Combat(BaseModel):
    """Combat Class"""
    def __init__(self, player, monster):
        """Init"""
        super().__init__()
        self.player = player
        self.monster = monster
        player_dmg = player.atk * (monster.df / 100)
        monster_dmg = monster.atk * (player.df / 100)
        save = monster.hp

        fighting = True
        while fighting:
            player.hp -= monster_dmg
            monster.hp -= player_dmg
            if player.hp <= 0 or monster.hp <= 0:
                fighting = False
        if player.hp > monster.hp:
            winner = player
        else:
            winner = monster
        if winner == monster:
            print("You lost :(")
            player.hp = 100
            monster.hp = save
        else:
            print("You won :D")
            player.hp = 100
            monster.hp = save
            player.add_exp(monster.exp)
            
            number = randint(1, 5)
            result = []
            i = 1
            while i < number:
                result.append(choice(monster.drops))
                i += 1
            for item in result:
                inventory.add(item)
                print("You got", item.name)
            player.levelup()