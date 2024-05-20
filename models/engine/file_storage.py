#!/usr/bin/python3
import json
import os

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__class__.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__class__.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__class__.__objects.items()}
        with open(self.__class__.__file_path, 'w') as file:
            json.dump(obj_dict, file, indent=2)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)."""
        if os.path.exists(self.__class__.__file_path):
            with open(self.__class__.__file_path, 'r') as file:
                try:
                    obj_dict = json.load(file)
                except json.JSONDecodeError:
                    return
                from models.base_model import BaseModel  # Avoid circular import issues
                classes = {
                    'BaseModel': BaseModel,
                    # Add other model classes here if needed
                }
                for key, value in obj_dict.items():
                    cls_name  = value['__class__']
                    cls =  classes.get(cls_name)
                    if cls:
                        obj = cls(**value)
                        self.__objects[key] = obj