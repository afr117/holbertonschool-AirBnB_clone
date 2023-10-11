#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def to_dict(self):
        """Return a dictionary containing keys/values of the User instance."""
        dict_rep = {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "email": self.email,
            "password": self.password,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "__class__": self.__class__.__name__
        }
        return dict_rep

