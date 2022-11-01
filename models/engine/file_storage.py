#!/usr/bin/python3
""" """
import json
from models.base_model import BaseModel


class FileStorage:
    """A class that serializes an instance to a JSON file
        and deserializes a JSON file to an intance

        Attributes:
            __file_path (string) : Private class attribute, string -path
                    to JSON file
            __objects (dict) : Private class attribute, dictionary,
                    will store all objects <class name>.id ex. Basemodel.11010
        Methods:
            all(self) : Returns the dictionary of __objects
            new(self) : sets in __objects with key <obj class name>.id
            save(self) : serializes __objects to JSON file( path: __file_path)
            reload(self) : deserializes JSON file to __objects, only if
                    JSON file(__file_path) exists, else if file doesn't
                    exists no exceptions should be raised
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary of __objects"""
        return type(self).__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        attr = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[attr] = obj

    def save(self):
        """Serializes __objects to JSON file (path: __file_path)"""
        j_dict = self.__objects

        new_dict = {obj: j_dict[obj].to_dict() for obj in j_dict.keys()}

        with open(self.__file_path, mode='w', encoding='utf-8') as new_file:
            json.dump(new_dict, new_file)

    def reload(self):
        """Deserializes JSON fileto __objects, only if JSON
            file(__file_path) exists, else if file doesn't
            exists no exceptions should be raised"""
        try:
            with open(self.__file_path, mode='r',
                      encoding='utf-8') as reload_file:
                all_objs = json.load(reload_file)

                for key, value in all_objs.items():
                    class_names = value['__class__']
                    self.__objects[key] = eval(class_names)(**value)
        except FileNotFoundError:
            return
