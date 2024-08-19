#!/usr/bin/python3
"""File Storage class definition"""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review

class FileStorage:

    """Has methods to serialize and deserialize objects"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        m_dict = {}
        for k, v in FileStorage.__objects.items():
            m_dict[k] = v.to_dict().copy()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(m_dict, f)


    def reload(self):
        """Reloads the stored objects"""
        try:
            with open(FileStorage.__file_path, mode='r') as f:
                m_dict = json.load(f)
            for k, v in m_dict.items():
                class_name = v.get(__class__)
                obj = eval(class_name + '(**v)')
                FileStorage.__objects[k] = obj
        except FileNotFoundError:
            pass
