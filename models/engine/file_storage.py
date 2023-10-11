#!/usr/bin/python3

import json
import os
import datetime
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    __file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'file.json')
    __objects = {}

    all_classes = {
        'BaseModel': BaseModel,
        'User': User
    }

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serializable_objects = {}
        for key, value in FileStorage.__objects.items():
            obj_dict = value.to_dict()
            serializable_objects[key] = obj_dict

        with open(self.__file_path, 'w') as file:
            json.dump(serializable_objects, file, default=str)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

