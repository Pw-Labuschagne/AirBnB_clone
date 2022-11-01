#!/usr/bin/python3
"""All possible places"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Plublic instance of the place with
        Attributes:
            city_id (string) = City.id
            user_id (string) = User.id
            name (string) = Name of place
            description (string) = Description of place
            number_rooms (integer) = Number of rooms
            number_bathrooms (integer) = Number of bathrooms
            max_guest (integer) = Max ammount of guests
            price_per_night (integer) = Price per night
            latitude (float) = Coordinates for latitude
            longitude (float) = Coordinates for longitude
            amenity_ids (list, string) = list of amenities
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_per_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = {}
