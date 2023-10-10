import os
from models.engine.file_storage import FileStorage

print("Running as root:", os.geteuid() == 0)

# Create a unique FileStorage instance for your application
storage = FileStorage()

# If the JSON file exists, call the reload method to load objects
if os.path.exists(FileStorage._FileStorage__file_path):
    storage.reload()

