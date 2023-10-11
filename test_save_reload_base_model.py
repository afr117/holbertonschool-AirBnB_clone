#!/usr/bin/python3

import os
from models import storage
from models.base_model import BaseModel

# Check if the storage object is properly initialized
if storage is None:
    print("Storage object is not properly initialized.")
else:
    print("Storage object is properly initialized.")

# Reload objects from the JSON file
storage.reload()

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

# Save the updated objects to the JSON file
storage.save()

# Check if the JSON file exists
print("After saving, checking if the JSON file exists:")
if os.path.exists(storage._FileStorage__file_path):
    print("JSON file exists.")
    with open(storage._FileStorage__file_path, 'r', encoding='utf-8') as file:
        data = file.read()
        print(data)
else:
    print("JSON file does not exist.")

