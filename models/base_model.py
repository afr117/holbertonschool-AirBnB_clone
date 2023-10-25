#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """
    This is the BaseModel class that defines common attributes/methods for other classes.
    """
    def __init__(self):
        """
        Initializes a new BaseModel instance with a unique ID and timestamps.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        Format: "[<class name>] (<self.id>) <self.__dict__>"
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance with the desired key order and ISO format for timestamps.
        """
        class_name = self.__class__.__name__
        key_order = ['my_number', 'name', '__class__', 'updated_at', 'id', 'created_at']

    # Format timestamps to ISO format strings
        updated_at_iso = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
        created_at_iso = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]

    # Convert class types to strings
        class_type_str = str(self.__class__)
        updated_at_type_str = str(type(self.updated_at))
        created_at_type_str = str(type(self.created_at))

    # Construct ordered dictionary
        ordered_dict = {
            '__class__': class_type_str,
            'id': self.id,
            'created_at': created_at_iso,
            'updated_at': updated_at_iso,
            '__class__': class_type_str,
            '__updated_at__': updated_at_type_str,
            '__created_at__': created_at_type_str,
            **self.__dict__
    }

    # Create a dictionary with the desired key order
        sorted_dict = {k: ordered_dict[k] for k in key_order}
        return sorted_dict


