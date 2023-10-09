#!/usr/bin/python3
"""
Module Doc: Base Class for all other classes
"""
import json
import datetime
import uuid


class BaseModel:
    """
    class Doc: Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        function Desc:  init
        """
        if id is None:
            BaseModel.__nb_objects += 1
            self.my_number = BaseModel.__nb_objects
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
        else:
            self.id = id
            self.class_type = self.__class__

    def __str__(self):
        """Override string to provide a better description."""
        # Create the ordered dictionary based on the desired order
        desired_order = ["my_number", "name",  "__class__", "updated_at", "id",
                         "created_at"]
        ordered_dict = {key: self.__dict__[key] for key in desired_order
                        if key in self.__dict__}

        return f"[{self.__class__.__name__}]({self.id}){ordered_dict}"

    def save(self):
        """update public instance attribute updated_at by current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return dictionary contains keys/values, __dict__, the instance """
        dict_rep = self.__dict__.copy()
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        # Add the class type
        dict_rep['__class__'] = self.__class__.__name__

        desired_order = ["my_number", "name", "__class__", "updated_at",
                         "id", "created_at"]
        ordered_dict = {key: dict_rep[key] for key in desired_order
                        if key in dict_rep}
        return ordered_dict
