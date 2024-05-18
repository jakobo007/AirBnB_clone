#!/usr/bin/python3
import json
import os



class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dictionary __objects"""
        return self.__class__.__objects

    def new(self,obj):
        """Sets in __objects the obj with key <obj classname>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__class__.__objects[key] = obj
        
    def save(self):
        """Serializes __objects to the JSON file(path:__file_path)"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__class__.__objects.items()}
        with open(self.__class__.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects(Only if the JSON file exists)"""
        """Otherwise do Nothing"""
        if os.path.exists(self.__class__.__file_path):
                with open(self.__class__.__file_path, 'r') as file:
                    try:
                        obj_dict = json.load(file)
                    except json.JSONDecodeError:
                        # Handle empty file or invalid JSON data
                        return
                    for key, value in obj_dict.items():
                        cls_name, obj_id = key.split('.')
                        cls = globals()[cls_name]
                        obj = cls(**value)
                        self.__class__.__objects[key] = obj