#!/usr/bin/python3
"""
Class BaseModel
Contains the Base class for the AirBnB clone console
"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """ Base Model """

    def __init__(self, *args, **kwargs):
        """ Initialization of a Base instance.
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    time = "%Y-%m-%dT%H:%M:%S.%f"
                    val = datetime.strptime(kwargs[key], time)
                if key != '__class__':
                    setattr(self, key, val)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns the str representation """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attribute
        updated_at with the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of
        __dict__ of the instance
        """

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
