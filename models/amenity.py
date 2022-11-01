#!/usr/bin/python3
"""Defines the amenities of the certain instance of basemodel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines the amenity
        Attributes:
            name (string) = Name of amenity
    """
    name = ""
