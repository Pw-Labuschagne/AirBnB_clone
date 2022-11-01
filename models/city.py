#!/usr/bin/python3
"""City in which the instance of basemodel is located"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines the city
            Attributes:
                state_id (string) = Used as a refrence to city
                name (string) = name of the city
    """

    state_id = ""
    name = ""
