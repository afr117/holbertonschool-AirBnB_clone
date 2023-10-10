#!/usr/bin/python3

import json
import os  # Import the os module
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
        serializable_objects = {}

        for key, value in self.__objects.items():
            # Convert the object's dictionary to a serializable format
            obj_dict = value.to_dict()
            serializable_objects[key] = obj_dict

        with open(self.__file_path, 'w') as file:
            json.dump(serializable_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    # Convert string representation back to datetime objects using strptime
                    if 'created_at' in value:
                        value['created_at'] = datetime.datetime.strptime(value['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    if 'updated_at' in value:
                        value['updated_at'] = datetime.datetime.strptime(value['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    class_name, obj_id = key.split('.')
                    obj = BaseModel(**value)

