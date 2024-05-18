#!/usr/bin/python3
"""Imported modules"""
import uuid
import datetime
from models import storage


class BaseModel:
    """Our base model that defines attributes for other classes"""
    
    def __init__(self, *args, **kwargs):

        """Attribute initialization"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)

            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.datetime.now()
                self.updated_at = datetime.datetime.now()
                storage.new(self)
            
            
    def save(self):
        """Updates the instance updated_at with current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()
        
    def to_dict(self):
        """Returns a dictionary containing all the key value pairs"""
        obj_dict = self.__dict__.copy()
        obj_dict ['__class__'] = self.__class__.__name__
        obj_dict ['created_at'] = self.created_at.isoformat()
        obj_dict ['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    
    def __str__(self):
        """Method for our desired print format"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"