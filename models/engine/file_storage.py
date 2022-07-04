#!/usr/bin/python3
"""Module for FileStorage class."""

import json
import os.path
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Serializes instances to a JSON file and deserializes
    JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the __objects dictionary"""

        return self.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""

        if obj is not None:
            key = obj.__class.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file"""

        with open(self.__file_path, "w", encoding="utf-8") as f:
            dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects"""

        my_dict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    self.__objects[k] = my_dict[v['__class__']](**v)
        except FileNotFoundError:
            pass
