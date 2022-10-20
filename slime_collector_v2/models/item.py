#!/usr/bin/python3
"""Contains class Item"""
from models.base_model import BaseModel


class Item(BaseModel):
    """Item class"""

    def __init__(self, name, type):
        """Init"""
        super().__init__()
        self.name = name
        self.type = type
