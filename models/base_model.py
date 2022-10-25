#!/usr/bin/python3
"""Base model that defines all common attributes/methods for other classes"""

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
    def __init__(self, name, id):
        """Instance of BaseModel"""
        self.name = name
        self.id = uuid.uuid4()

    def __str__(self):
        """Print method"""
        print("[{}] ({}) {}".format(self.name, self.id, self.__dict__))
        
