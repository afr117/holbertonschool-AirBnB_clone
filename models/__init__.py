#!/usr/bin/python3

def __init__(self, *args, **kwargs):
    """Initialize the BaseModel instance."""
    if kwargs:
        for key, value in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
                setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
            else:
                setattr(self, key, value)
    else:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

