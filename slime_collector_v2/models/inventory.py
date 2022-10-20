#!/usr/bin/python3
"""Contains class Inventory"""
from models.base_model import BaseModel


class Inventory(BaseModel):
    """Inventory Class"""

    def __init__(self):
        """Init"""
        super().__init__()
        self.inventory = []

    def add(self, item):
        """Adds item to inventory"""
        self.inventory.append(item)

    def remove(self, item):
        """Removes item from inventory"""
        self.inventory.remove(item)

    def display(self):
        """Displays inventory"""
        print("In your inventory, you have:")
        for item in self.inventory:
            print(item.name)

inventory = Inventory()

slime_collection = Inventory()
