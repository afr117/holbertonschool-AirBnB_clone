import os
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()

# If the JSON file exists, call the reload method to load objects
if os.path.exists(FileStorage._FileStorage__file_path):
    storage.reload()

