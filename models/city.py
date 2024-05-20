#!/usr/bin/python3
"""Imported modules"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""

    state_id: str = ""
    name: str = ""
    def __init__(self, *args, **kwargs):
        """Initialize the city Instances"""
        super().__init__(*args, **kwargs)