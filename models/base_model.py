#!/usr/bin/python3
"""
Module Doc: Base Class for all other classes
"""

import json
import datetime
import uuid
import os

class BaseModel:
    """
    class Doc: Base Class
    """
    __nb_objects = 0

    def __init__(self, *args, **kwargs):
        """
        function Desc:  init
        """
        from models import storage  # Import here to avoid circular import
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at") and isinstance(value, str):
                        setattr(self, key, datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            BaseModel.__nb_objects += 1
            self.my_number = BaseModel.__nb_objects
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
            storage.new(self)

    def __str__(self):
        """Override string to provide a better description."""
        return f"[{self.__class__.__name__}]({self.id}) {self.to_dict()}"

    def save(self):
        """update public instance attribute updated_at by the current datetime"""
        from models import storage  # Import here to avoid circular import
        self.updated_at = datetime.datetime.now()
        storage.save()  # Use the storage module here

    def to_dict(self):
        """Return a dictionary containing keys/values, __dict__, the instance"""
        dict_rep = {
            "my_number": self.my_number,
            "name": getattr(self, "name", ""),
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "id": self.id,
            "created_at": self.created_at.isoformat()
        }
        return dict_rep

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")

    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")

    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")

    print(my_model is my_new_model)

