#!/usr/bin/python3

import json
import os
import datetime
from models.base_model import BaseModel

class FileStorage:
    __file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'file.json')
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serializable_objects = {} 
        for key, value in FileStorage.__objects.items():
            obj_dict = value.to_dict()
            serializable_objects[key] = obj_dict

        with open(self.__file_path, 'a') as file:
            if file.tell() != 0:
                file.write('\n')

            json.dump(serializable_objects, file, default=str)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

