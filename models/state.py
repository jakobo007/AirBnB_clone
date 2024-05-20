#!/usr/bin/python3
"""Imported modules"""
from models.base_model import BaseModel


class State(BaseModel):
    """class state that inherits from BaseModel"""
    name: str = ""
    def __init__(self, *args, **kwargs):
        """Initialize state instances"""
        super().__init__(*args, **kwargs)
    