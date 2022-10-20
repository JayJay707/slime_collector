#!/usr/bin/python3
"""Contains class Region"""
from models.base_model import BaseModel


class Region(BaseModel):
    """Region class"""

    def __init__(self, name, item_list):
        """Init"""
        super().__init__()
        self.name = name
        self.item_list = item_list
    
    def info(self, name):
        """Displays info about the region"""
        if name == "Forest":
            print("A large, peaceful forest with little to no monsters.")
            print("Items:")
            for item in self.item_list:
                print(item.name)
