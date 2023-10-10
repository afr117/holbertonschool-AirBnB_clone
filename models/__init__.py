import os
from .engine.file_storage import FileStorage

print("Running as root:", os.geteuid() == 0)

# Create a unique FileStorage instance for your application
storage = FileStorage()
storage.reload()

