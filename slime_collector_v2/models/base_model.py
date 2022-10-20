#!/usr/bin/python3
"""Base Module"""
from uuid import uuid4


class BaseModel:
    """Base class"""

    def __init__(self):
        """init method"""
        self.id = str(uuid4())
