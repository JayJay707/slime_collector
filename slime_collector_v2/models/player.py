#!/usr/bin/python3
"""Contains player class"""
from models.base_model import BaseModel


class Player(BaseModel):
    """Player Class"""
    def __init__(self):
        """Init"""
        super().__init__()
        self.name = None
        self.hp = 100
        self.atk = 15
        self.df = 30
        self.lvl = 0
        self.exp = 0

    def set_name(self, name):
        """Set the player's name"""
        self.name = name
    
    def levelup(self):
        if self.exp >= 100:
            self.lvl += 1
            self.hp += 5
            self.atk += 5
            self.df += 5
            self.exp = 0
            print("Congrats! You've leveled up :D")
    
    def add_exp(self, add):
        self.exp += add
    
    def info(self):
        print(self.name, "| Level:", self.lvl, "(", self.exp, ")")
        print("HP:", self.hp)
        print("Attack:", self.atk)
        print("Defense:", self.df)

player = Player()
