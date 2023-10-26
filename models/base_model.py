#!/usr/bin/python3
"""Defines the BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents BaseModel class all others inherit from"""

    def __init__(self, *args, **kwargs):
        """ Initializes a BaseModel
        Param Args: Args - list of arguments
        kwargs - dictionary of key:value arguments
        """

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            FileStorage.new(self)
		
    def __str__(self):
	    """print/str representation of BaseModel instance"""
	    cls_name = type(self).__name__
	    str_rep = "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
	    return (str_rep)
	    
    def save(self):
	    """Updates updated_at with current time"""
	    self.updated_at = datetime.now()
	    FileStorage.save()

    def to_dict(self):
	    """returns dictionary key/value list of __dict__"""
	    dict_rep = {}
	    time_format = datetime.isoformat
	    for key in self.__dict__:
		    value = self.__dict__[key]
		    if key == "created_at" or key == "updated_at":
			    dict_rep[key] = str(time_format(value))
		    else:
			    dict_rep[key] = value
			    dict_rep["__class__"] = type(self).__name__
			    return dict_rep
