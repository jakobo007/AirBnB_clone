#!/usr/bin/python3
"""Imported modules"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel"""

    place_id: str = ""
    user_id: str = ""
    text: str = ""

    def __init__(self, *args, **kwargs):
        """Initialize the Review Instance"""
        super().__init__(*args, **kwargs)