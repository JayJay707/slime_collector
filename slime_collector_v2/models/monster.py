#!/usr/bin/python3
"""Contains class monster"""
from models.base_model import BaseModel
from models.regions_items import *


class Monster(BaseModel):
    """Class Monster"""
    def __init__(self, name, hp, atk, df, exp, *drops):
        """Init"""
        super().__init__()
        self.name = name
        self.hp = hp
        self.atk = atk
        self.df = df
        self.exp = exp
        self.drops = drops
