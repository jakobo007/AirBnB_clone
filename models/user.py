#!/usr/bin/python3
"""Imported modules"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class user that inherits from BaseModel"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    def __init__(self, *args, **kwargs):
        """Initialize the User Instance"""
        super().__init__(*args, **kwargs)