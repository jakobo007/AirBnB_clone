#!/usr/bin/python3
"""Imported Modules"""
from models.base_model import BaseModel

class Place(BaseModel):
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int  = 0
    price_by_night = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: str = []

    def __init__(self, *args, **kwargs):
        """Initialize the Place Instances"""
        super().__init__(*args, **kwargs)