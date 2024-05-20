#!/usr/bin/python3
"""Imported modules"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class that inherits from BaseModel"""

    name: str = ""
    def __init__(self, *args, **kwargs):
        """Initialize the amenity Instance"""
        super().__init__(*args, **kwargs)