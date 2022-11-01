#!/usr/bin/python3
"""Class used to store users"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents User
        Attributes:
            email (string) = Email of user
            password (sting) = Password of user
            first_name (string) = First name of user
            last_name (string) = Last_name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
