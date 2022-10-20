#!/usr/bin/python3
"""Contains class Slime"""
from random import choice
from models.base_model import BaseModel
from models.inventory import inventory


class Slime(BaseModel):
    """Slime class"""

    def __init__(self):
        """Init"""
        super().__init__()
        self.type = ["Neutral", "Neutral"]
        self.name = self.type[0] + "Slime"
        self.evolution = 0

    def set_name(self, name):
        """Name the slime"""
        self.name = name

    def feed(self, item):
        """Feed the slime"""
        if self.evolution == 0:
            self.type[1] = item.type
            inventory.remove(item)
            self.evolution += 10
        elif self.evolution != 0 and self.evolution != 100:
            if item.type != self.type[1]:
                print("You can't feed this item to your slime as you have already fed it a", self.type[1], "item.")
            else:
                self.evolution += 10
                inventory.remove(item)
        if self.evolution == 100:
            self.type[0] = self.type[1]
            print("Congratulations! Your slime has evolved into a", self.type[0], "slime!")

    def info(self):
        """Displays info about the slime"""
        print(self.name, "| Type:", self.type, "| Evolution status:", self.evolution)

    def pet(self):
        """Pet the slime"""
        result = ["happy", "angry", "shy", "satisfied", "content", "sleepy and falls asleep under your touch", "hungry and tries to bite your hand"]
        print(self.name, "is", choice(result), "!")
