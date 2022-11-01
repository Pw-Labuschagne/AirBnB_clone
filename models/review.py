#!/usr/bin/python3
"""Review instance of basemodel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines reviews made on location
        Attributes:
            place_id (string) = Id of the place
            user_id (string) = User that made review
            text (string) = Review made
    """

    place_id = ""
    user_id = ""
    text = ""
