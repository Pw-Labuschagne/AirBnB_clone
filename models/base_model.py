#!/usr/bin/python3
"""Base model that defines all common attributes/methods for other classes"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:

    """
        Attributes:
            id (string) = Assign with uuid
            created_at (datetime) = Assign with current date and time when
                when instance is created
            updated_at (datetime) = Assing with current date and time when
                instance is updated (every time)
            __str__ (string) = Should print [<class name>] (<self.id>)
                               <self.__dict__>
        Methods:
            Save(self) = Update public instance attribute updated_at with
            current datetime
            to_dict(self) = Returns dictonary containing all keys/values
                of __dict__ of instance
    """
    def __init__(self, *args, **kwargs):
        """Instance of BaseModel
            constructor of basemodel = *args and **kwargs
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """
            Used to save public instance attribute updated_at with
            current datetime
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
            Used to return dictonary containing all keys/values
            of __dict__ of instance:
            Using self.__dict__ = only instance attr will be returned
            a key __class__ must be added to dictonary with class anme of obj

            created_at and updated_at must be converted to ISO format:
            %Y-%m-%dT%H:%M:%S.%f ex. 2017-06-14T22:31:03.285259
            We can use isoformat() for datetime obj
        """
        ndict = self.__dict__.copy()
        ndict["created_at"] = self.created_at.isoformat()
        ndict["updated_at"] = self.updated_at.isoformat()
        ndict["__class__"] = self.__class__.__name__

        return ndict

    def __str__(self):
        """Print method"""
        clsname = self.__class__.__name__
        return("[{}] ({}) {}".format(clsname, self.id, self.__dict__))
